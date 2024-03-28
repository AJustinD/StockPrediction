import streamlit as st
import os
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import make_scorer, precision_score
from tensorflow.keras.models import load_model

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
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'svm_model.pkl'),
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'xgb_model.pkl'),
]
meta_model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'final_model.pkl')

# Load base models and meta model directly from the specified paths
base_models = [joblib.load(model_path) for model_path in base_model_paths]
meta_model = load_model(meta_model_path)

# Streamlit UI
st.title('Multiclass Classification App')

# Define and collect input features from the user
feature_names = ['Net Foreign Buy (Vol)', 'Net Domestic Buy (Vol)', 'Volume', 'Frequency']
features_input = []
default_values = [100000,-100000,1000000,15000]

for i, feature_name in enumerate(feature_names):  # Use custom feature names
    input_value = st.number_input(feature_name, value=default_values[i])
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

        # Meta-model prediction
        final_predictions = meta_model.predict(base_predictions_unseen)

        # Assuming the meta-model outputs class probabilities, get the labels
        final_predictions_labels = np.argmax(final_predictions, axis=1)

        # Display class labels and their corresponding index number
        st.subheader('Class labels and their corresponding index number')
        st.table(df_class_labels)

        # Display the prediction
        st.subheader('Prediction')
        st.write(f'Prediction: {df_class_labels["Class Label"].iloc[final_predictions_labels[0]]}')

        # Display Prediction Probabilities
        st.subheader('Prediction Probability')
        # Display the probabilities in a more interpretable way, if necessary
        # For example, you can display only the highest probability and corresponding class
        st.write(final_predictions)

else:
    st.error("Please fill in all the input fields.")
