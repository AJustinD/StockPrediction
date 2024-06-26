import streamlit as st
import os
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import make_scorer, precision_score

# Define the class Labels
class_labels = {
    'Index Number': [0, 1, 2, 3],
    'Class Label': ['Super-Down', 'Down', 'Up', 'Super-Up']
}
df_class_labels = pd.DataFrame(class_labels)

# Specify the local path to the scaler
scaler_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scaler.pkl')
# Load the scaler
scaler = joblib.load(scaler_path)

# Custom Function
def custom_precision_score(y_true, y_pred):
    return precision_score(y_true, y_pred, labels=[3], average='micro') if 3 in y_pred else 0

# Define local paths for your saved models using double backslashes to avoid escape sequence errors
base_model_paths = [
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dt_model.pkl'),
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lr_model.pkl'),
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'rf_model.pkl'),
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'knn_model.pkl'),
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'xgb_model.pkl')
]
meta_model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'final_model.pkl')

# Load base models and meta model directly from the specified paths
base_models = [joblib.load(model_path) for model_path in base_model_paths]
meta_model = joblib.load(meta_model_path)

# Streamlit UI
st.title('Multiclass Classification App')

feature_names = ['Net Foreign Buy (Vol)', 'Volume', 'Frequency']
default_values = [100000, 1000000, 15000]  # Assuming net foreign buy is typically negative

features_input = []

# Assuming 'Net Foreign Buy (Vol)' needs to be captured as 'Net_foreign_buy'
net_foreign_buy_vol = st.number_input('Net Foreign Buy (Vol)', value=default_values[0])
features_input.append(-float(net_foreign_buy_vol))  # Appending as 'Net_domestic_buy'

features_input.append(float(net_foreign_buy_vol))  # Appending as 'Net_foreign_buy'

# Collect the rest of the features
for i, feature_name in enumerate(feature_names[1:]):  # Start from 1 to skip 'Net Foreign Buy (Vol)'
    input_value = st.number_input(feature_name, value=default_values[i + 1])  # i + 1 because we've already handled index 0
    features_input.append(float(input_value))

# Predict button
if all(value is not None for value in features_input):
    # Proceed with prediction
    if st.button('Predict'):
        # Preprocess the input features
        X_unseen = np.array([features_input])
        X_unseen = scaler.transform(X_unseen)  # Use the loaded, pre-fitted scaler

        # Generate base model predictions
        base_predictions_unseen = np.column_stack([model.predict(X_unseen) for model in base_models])

        # Meta-model probability prediction
        final_probabilities = meta_model.predict_proba(base_predictions_unseen)

        predicted_label = df_class_labels['Class Label'][np.argmax(final_probabilities)]  # Get the label with the highest probability

        # Display class labels and their corresponding index number
        st.subheader('Class labels and their corresponding index number')
        st.write('Super-up : Above 5% | Super-down: Below -5%')
        st.table(df_class_labels)

        # Display the prediction
        st.subheader('Prediction')
        st.write(f'Prediction: {predicted_label}')

        # Display Prediction Probabilities
        st.subheader('Prediction Probability')
        # Display the probabilities for each class
        probability_data = pd.DataFrame(final_probabilities, columns=df_class_labels['Class Label'])
        st.write(probability_data)
else:
    st.error("Please fill in all the input fields.")
