# Telco Customer Churn Prediction: A Machine Learning Approach

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project demonstrates a **machine learning approach to predict customer churn** in a telecommunications company using the **Telco Customer Churn** dataset. By identifying at-risk customers early, telecom providers can implement targeted retention strategies to reduce churn and improve customer loyalty.

---

## 💾 Dataset

**Source:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`  
**Link:** [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

### Key Features:
- **Demographics**: `gender`, `SeniorCitizen`, `Partner`, `Dependents`
- **Services**: `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, etc.
- **Account Info**: `Contract`, `PaperlessBilling`, `PaymentMethod`, `MonthlyCharges`, `TotalCharges`
- **Target**: `Churn` (`Yes` / `No`)

---

## 📊 Data Workflow

### 1. **Exploratory Data Analysis (EDA)**
- Visualized feature distributions and relationships.
- Generated **Correlation Heatmap** to identify key predictors of churn.
- Key insights: `Contract`, `tenure`, and `MonthlyCharges` strongly correlate with churn.

### 2. **Data Cleaning**
- Converted `TotalCharges` from string to numeric.
- Handled missing/invalid values in `TotalCharges` (replaced with median or removed).
- Removed irrelevant column: `customerID`.

### 3. **Feature Engineering**
- **Label Encoding**: Converted `Churn` (`Yes` → 1, `No` → 0).
- **One-Hot Encoding**: Applied to categorical variables (`gender`, `Contract`, `PaymentMethod`, etc.).
- Final feature set ready for modeling.

### 4. **Train-Test Split**
- 80% Training | 20% Testing
- Stratified split to maintain class distribution.

---

## 🤖 Predictive Modeling

Two classification models were trained and evaluated:

---

### 1. **Logistic Regression**
> A baseline linear model for binary classification.

| Metric           | Value  |
|------------------|--------|
| **Accuracy**     | **79.1%** |

---

### 2. **Random Forest Classifier**
> Ensemble of decision trees; robust to overfitting and captures non-linear patterns.

| Metric           | Value  |
|------------------|--------|
| **Accuracy**     | **77.8%** |

#### Confusion Matrix (Random Forest)
