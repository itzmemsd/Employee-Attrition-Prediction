import streamlit as st
import pandas as pd

st.title("📑 Model Performance")

df = pd.read_csv(
    "results/model_comparison.csv"
)

st.dataframe(df)

st.image(
    "results/accuracy_comparison.png"
)

st.image(
    "results/confusion_matrix.png"
)

st.image(
    "results/roc_curve.png"
)