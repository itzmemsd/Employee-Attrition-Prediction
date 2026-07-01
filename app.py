import streamlit as st

st.set_page_config(
    page_title="Employee Attrition Analytics",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================
# HEADER
# ============================

st.markdown("""
# 🤖 Employee Attrition Analytics & AI Decision Support System
### Powered by Machine Learning | XGBoost | Streamlit

---
""")

st.write(
    """
Welcome to the **Employee Attrition Analytics Platform**.

This platform helps HR professionals predict employee attrition,
analyze workforce trends, and make data-driven decisions using
Artificial Intelligence.
"""
)

# ============================
# PROJECT HIGHLIGHTS
# ============================

st.markdown("## 🚀 Project Highlights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Employees",
        "1470"
    )

    st.metric(
        "Machine Learning Models",
        "7"
    )

with col2:
    st.metric(
        "Best Model",
        "XGBoost"
    )

    st.metric(
        "Accuracy",
        "88.10%"
    )

with col3:
    st.metric(
        "Dashboard Pages",
        "6"
    )

    st.metric(
        "Dataset Features",
        "30"
    )

st.markdown("---")

# ============================
# FEATURES
# ============================

st.markdown("## 📌 Key Features")

feature1, feature2 = st.columns(2)

with feature1:

    st.success("📊 Executive Dashboard")

    st.success("📈 Interactive Analytics")

    st.success("🤖 Employee Prediction")

    st.success("🧠 AI Recommendation Engine")

with feature2:

    st.success("📑 Model Performance")

    st.success("📉 ROC & Confusion Matrix")

    st.success("📁 Download Prediction")

    st.success("📊 Machine Learning Comparison")

st.markdown("---")

# ============================
# TECHNOLOGIES
# ============================

st.markdown("## 💻 Technologies")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.info("""
Python

Pandas

NumPy
""")

with tech2:
    st.info("""
Scikit-Learn

XGBoost

LightGBM

CatBoost
""")

with tech3:
    st.info("""
Streamlit

Plotly

Matplotlib
""")

st.markdown("---")

# ============================
# WORKFLOW
# ============================

st.markdown("## 🔄 Project Workflow")

st.code("""

Dataset

      │

      ▼

Data Cleaning

      │

      ▼

Feature Engineering

      │

      ▼

Machine Learning

      │

      ▼

Model Evaluation

      │

      ▼

Best Model Selection

      │

      ▼

Prediction Dashboard

      │

      ▼

AI Recommendation

""")

st.markdown("---")

# ============================
# NAVIGATION
# ============================

st.markdown("## 📂 Navigation")

st.write("➡️ Executive Dashboard")

st.write("➡️ Analytics Dashboard")

st.write("➡️ Employee Prediction")

st.write("➡️ Model Performance")

st.write("➡️ About")

st.markdown("---")

st.success(
    "Ready to explore the Employee Attrition Analytics Platform."
)

st.caption(
    "Developed by Dr. M. Sasidharan | Department of Management Studies | Shikshaa Institute of Advanced Technologies"
)