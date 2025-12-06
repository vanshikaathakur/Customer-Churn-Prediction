# 📞 Telco Customer Churn Prediction: A Machine Learning Approach

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project demonstrates a **machine learning approach to predict customer churn** in a telecommunications company using the **Telco Customer Churn** dataset. By identifying at-risk customers early, telecom providers can implement targeted retention strategies to reduce churn and improve customer loyalty.

---

## ✨ Deployment & Interface

To make the model usable, the project includes a **full deployment pipeline**:

1.  **FastAPI Prediction API**: A **REST API** built with **FastAPI** to serve real-time predictions. The API handles data preprocessing (scaling, encoding) and returns the churn prediction and probability.
2.  **Streamlit Web Interface**: A user-friendly graphical interface built with **Streamlit** that consumes the FastAPI predictions. Users can input customer data and instantly receive a churn probability and prediction. The image below shows the interface in action:


---

## 💾 Dataset

**Source:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`
**Link:** [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

### Key Features:
-   **Demographics**: `gender`, `SeniorCitizen`, `Partner`, `Dependents`
-   **Services**: `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, etc.
-   **Account Info**: `Contract`, `PaperlessBilling`, `PaymentMethod`, `MonthlyCharges`, `TotalCharges`
-   **Target**: `Churn` (`Yes` / `No`)

---

## 📊 Data Workflow

### 1. **Exploratory Data Analysis (EDA)**
-   Visualized feature distributions and relationships.
-   Generated **Correlation Heatmap** to identify key predictors of churn.
-   Key insights: `Contract`, `tenure`, and `MonthlyCharges` strongly correlate with churn. 
### 2. **Data Cleaning**
-   Converted `TotalCharges` from string to numeric.
-   Handled missing/invalid values in `TotalCharges` (replaced with median or removed).
-   Removed irrelevant column: `customerID`.

### 3. **Feature Engineering**
-   **Label Encoding**: Converted `Churn` (`Yes` → 1, `No` → 0).
-   **One-Hot Encoding**: Applied to categorical variables (`gender`, `Contract`, `PaymentMethod`, etc.).
-   Final feature set ready for modeling.

### 4. **Train-Test Split**
-   80% Training | 20% Testing
-   Stratified split to maintain class distribution.

---

## 🤖 Predictive Modeling

Two classification models were trained and evaluated, with **Logistic Regression** being chosen for its balance of interpretability and performance.

---

### 1. **Logistic Regression**
> A baseline linear model for binary classification, chosen for deployment due to robust performance and speed.

| Metric | Value |
| :--- | :--- |
| **Accuracy** | **79.1%** |

---

### 2. **Random Forest Classifier**
> Ensemble of decision trees; robust to overfitting and captures non-linear patterns.

| Metric | Value |
| :--- | :--- |
| **Accuracy** | **77.8%** |

#### Confusion Matrix (Random Forest)

---

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/vanshikaathakur/Customer-Churn-Prediction]
    cd telco-churn-prediction
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Start the FastAPI server:**
    ```bash
    uvicorn api.main:app --reload
    ```
    *The API will be running on `http://127.0.0.1:8000`.*

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    *The app will open in your browser on `http://localhost:8501`.*
