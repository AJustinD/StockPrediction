import streamlit as st
import datetime
import yfinance as yf, pandas as pd, numpy as np
import plotly.express as px
from stocknews import StockNews
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from datetime import date
import json


st.title('Stock Dashboard')
stocks = ('ASII.JK','ACES.JK','ADRO.JK','ANTM.JK','AMRT.JK','BBCA.JK','BBTN.JK','BMRI.JK','BBNI.JK','BBRI.JK','BUKA.JK',
	  'BRIS.JK','BREN.JK','BRPT.JK','BYAN.JK','CUAN.JK','CPIN.JK','DCII.JK','GOTO.JK','GGRM.JK','HSMP.JK','INDF.JK','ITMG.JK',
	  'KLBF.JK','MBMA.JK','MDKA.JK','MEDC.JK','PGAS.JK','PTBA.JK','SIDO.JK','TPIA.JK','TLKM.JK','TOWR.JK','UNTR.JK','UNVR.JK')
ticker = st.selectbox('Select dataset for prediction', stocks)
start_date = st.date_input('Start Date', datetime.date(2024, 1, 1))
end_date = st.date_input('End Date', datetime.date.today())

data = yf.download(ticker,start = start_date, end= end_date)
fig = px.line(data, x= data.index, y = data['Adj Close'], title = ticker)
st.plotly_chart(fig)

def load_comments(ticker):
    try:
        with open(f"{ticker}_comments.json", "r") as file:
            comments = json.load(file)
    except FileNotFoundError:
        comments = []
    return comments

def save_comment(ticker, comment):
    comments = load_comments(ticker)
    comments.append(comment)
    with open(f"{ticker}_comments.json", "w") as file:
        json.dump(comments, file)

pricing_data , fundamental_data, news, forum = st.tabs(["Price Data", "Fundamental Data", "Top 10 News", "Discussion Forum"])

with pricing_data:
    st.header('Price Movement')
    data2 = data
    data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    data2.dropna(inplace = True)
    st.write(data2)
    annual_return = round(data2['% Change'].mean() * 252 * 100, 2)
    st.write('Annual Return is ', annual_return, '%')
    stdev = round(np.std(data2['% Change']) * np.sqrt(252) * 100,2)
    st.write('Standard Deviation is ', stdev, '%') # Volatility
    risk_adj_return = round(annual_return / stdev, 2) if stdev != 0 else 0
    st.write('Risk Adj. Return is ', risk_adj_return)


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
with forum:
    st.header(f"Discussion Forum for {ticker}")

    # Load and display comments
    comments = load_comments(ticker)
    for comment in comments:
        st.text_area("", comment, disabled=True, height=75)

    # Input for new comment
    new_comment = st.text_area('Add your discussion')

    # Button to post a new comment
    if st.button('Post Comment'):
        if new_comment:
            save_comment(ticker, new_comment)
            st.success('Comment posted successfully!')
            # Rerun the app to update the comments display
            st.experimental_rerun()
        else:
            st.error('Please enter a comment before posting.')

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
st.write(forecast.tail(period))

st.write(f'Forecast plot for {n_months} months')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.pyplot(fig2)
