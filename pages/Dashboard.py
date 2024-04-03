import streamlit as st
import datetime
import yfinance as yf, pandas as pd, numpy as np
import plotly.express as px
from alpha_vantage.fundamentaldata import FundamentalData
from stocknews import StockNews
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from datetime import date


st.title('Stock Dashboard')
stocks = ('BBCA.JK', 'BBRI.JK', 'TLKM.JK', 'ASII.JK')  # Use Indonesian stock market symbols
ticker = st.selectbox('Select dataset for prediction', stocks)
start_date = st.date_input('Start Date', datetime.date(2024, 1, 1))
end_date = st.date_input('End Date', datetime.date.today())

data = yf.download(ticker,start = start_date, end= end_date)
fig = px.line(data, x= data.index, y = data['Adj Close'], title = ticker)
st.plotly_chart(fig)

pricing_data , fundamental_data, news = st.tabs(["Price Data", "Fundamental Data", "Top 10 News"])

with pricing_data:
    st.header('Price Movement')
    data2 = data
    data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    data2.dropna(inplace = True)
    st.write(data2)
    annual_return = data2['% Change'].mean() * 252 * 100
    st.write('Annual Return is ', annual_return, '%')
    stdev = np.std(data2['% Change']) * np.sqrt(252)
    st.write('Standard Deviation is ', stdev*100, '%') # Volatility
    st.write('Risk Adj. Return is ', annual_return/ (stdev*100))

with fundamental_data:
    ticker_data = yf.Ticker(ticker)

    st.subheader('Balance Sheet')
    balance_sheet = ticker_data.balance_sheet
    st.dataframe(balance_sheet)

    st.subheader('Income Statement')
    income_statement = ticker_data.financials
    st.dataframe(income_statement)

    st.subheader('Cash Flow Statement')
    cash_flow = ticker_data.cashflow
    st.dataframe(cash_flow)

with news:
    st.header(f'News of {ticker}')
    sn = StockNews(ticker, save_news=False)
    df_news = sn.read_rss()

    for i in range(10):
        st.subheader(f'News {i+1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.write(f'Title Sentiment {title_sentiment}')
        news_sentiment = df_news['sentiment_summary'][i]
        st.write(f'News Sentiment {news_sentiment}')

START = "2020-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.subheader('Price Outlook')

n_months = st.slider('Months of prediction:', 1, 12)  # Slider for months instead of years
period = n_months * 30  # Approximate each month as 30 days

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(ticker)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)

plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader(f'Forecast data for {ticker}')
st.write(forecast.tail())

st.write(f'Forecast plot for {n_months} months')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.pyplot(fig2)
