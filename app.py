import streamlit as st
import requests
import json
import pandas as pd

# Define the API endpoint URL
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Churn Predictor", layout="wide")
st.title("🎯 Customer Churn Prediction Dashboard")
st.markdown("---")

# --- 1. Collect User Input ---

st.header("👤 Customer Data Input")

# Create two columns for a cleaner layout
col1, col2, col3 = st.columns(3)

# --- Customer Profile Features (Numerical & Binary) ---
with col1:
    st.subheader("Profile")
    # Numerical
    tenure = st.slider("Tenure (Months)", 1, 72, 24, help="Number of months the customer has been with the company.")
    
    # Binary/Categorical
    senior_citizen = st.checkbox("Senior Citizen", value=False)
    partner = st.checkbox("Has Partner", value=True)
    dependents = st.checkbox("Has Dependents", value=False)
    phone_service = st.checkbox("Phone Service", value=True)
    multiple_lines = st.checkbox("Multiple Lines (if Phone Service is On)", value=True)

# --- Services Features (Binary) ---
with col2:
    st.subheader("Services Subscribed")
    
    # Internet Service Dropdown (Handles one-hot encoding below)
    internet_service_type = st.selectbox("Internet Service Type", ["Fiber optic", "DSL", "No"], index=0)

    online_security = st.checkbox("Online Security", value=False)
    online_backup = st.checkbox("Online Backup", value=True)
    device_protection = st.checkbox("Device Protection", value=False)
    tech_support = st.checkbox("Tech Support", value=False)
    streaming_tv = st.checkbox("Streaming TV", value=True)
    streaming_movies = st.checkbox("Streaming Movies", value=True)


# --- Billing & Payment Features (Numerical & Categorical) ---
with col3:
    st.subheader("Billing & Contract")
    
    # Numerical
    monthly_charges = st.number_input("Monthly Charges ($)", 18.0, 150.0, 85.50, step=0.01)

    # Categorical Inputs
    contract = st.selectbox("Contract Type", [1, 2, 3], format_func=lambda x: {1: "Month-to-month", 2: "One year", 3: "Two year"}[x])
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Credit card (automatic)", "Mailed check", "Bank transfer (automatic)"])
    paperless_billing = st.checkbox("Paperless Billing", value=True)


st.markdown("---")

# --- 2. Format the Payload and Execute ---

if st.button("🚀 Get Churn Prediction", type="primary"):
    
    # --- A. Handle One-Hot Encoding for the Payload ---
    
    # Internet Service Encoding (Based on your 3 features)
    is_fiber_optic = 1 if internet_service_type == "Fiber optic" else 0
    is_no_internet = 1 if internet_service_type == "No" else 0
    
    # Payment Method Encoding (Based on your 3 features, assuming Bank Transfer is the 'missing' reference category)
    pm_credit_card = 1 if payment_method == "Credit card (automatic)" else 0
    pm_electronic_check = 1 if payment_method == "Electronic check" else 0
    pm_mailed_check = 1 if payment_method == "Mailed check" else 0
    
    # NOTE on Contract: We use the numerical value for contract (1, 2, or 3) assuming your model was trained that way. 
    # If your model used one-hot encoding for Contract, this part needs adjustment (e.g., Contract_Month-to-month: 1/0).

    
    # Construct the payload dictionary with ALL 21 features (Must match the exact feature names!)
    payload = {
        "SeniorCitizen": 1 if senior_citizen else 0,
        "Partner": 1 if partner else 0,
        "Dependents": 1 if dependents else 0,
        "tenure": float(tenure), 
        "PhoneService": 1 if phone_service else 0,
        "OnlineSecurity": 1 if online_security else 0,
        "OnlineBackup": 1 if online_backup else 0,
        "DeviceProtection": 1 if device_protection else 0,
        "TechSupport": 1 if tech_support else 0,
        "StreamingTV": 1 if streaming_tv else 0,
        "StreamingMovies": 1 if streaming_movies else 0,
        "Contract": float(contract), # Assuming numerical value is used
        "PaperlessBilling": 1 if paperless_billing else 0,
        "MonthlyCharges": float(monthly_charges),
        "MultipleLines_Yes": 1 if multiple_lines else 0,
        "InternetService_Fiber optic": is_fiber_optic,
        "InternetService_No": is_no_internet,
        "PaymentMethod_Credit card (automatic)": pm_credit_card,
        "PaymentMethod_Electronic check": pm_electronic_check,
        "PaymentMethod_Mailed check": pm_mailed_check
        # If your model required the Gender feature, you'll need to add it here too!
    }
    
    # --- B. Call the API and Display Result ---
    
    try:
        # Send the POST request to your FastAPI endpoint
        response = requests.post(API_URL, json=payload)
        
        # Check if the API call was successful (HTTP status code 200)
        if response.status_code == 200:
            result = response.json()
            
            prediction = result.get("churn_prediction")
            probability = result.get("churn_probability")
            
            st.success("✅ Prediction Received!")
            st.markdown(f"**Customer Churn Probability:** **{probability:.2f}** ({probability*100:.1f}%)")
            
            if prediction == 1:
                st.error("🚨 **CHURN ALERT**: This customer is predicted to leave the company.")
            else:
                st.info("🟢 **STABLE**: This customer is predicted to stay.")
        
        else:
            st.error(f"API Error: Could not get prediction. Status code: {response.status_code}")
            st.code(response.text) # Show raw error from FastAPI for debugging

    except requests.exceptions.ConnectionError:
        st.error("Connection Error: Failed to connect to the FastAPI service. Please ensure the API is running in another terminal at http://127.0.0.1:8000.")