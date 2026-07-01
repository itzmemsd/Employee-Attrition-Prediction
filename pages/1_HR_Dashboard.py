from src.insights import generate_insights
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="HR Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 HR Executive Dashboard")

df = pd.read_csv(
    "dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# ======================================================
# KPI SECTION
# ======================================================

employees = len(df)

employees_left = len(
    df[df["Attrition"] == "Yes"]
)

employees_stayed = len(
    df[df["Attrition"] == "No"]
)

attrition_rate = (
    employees_left / employees
) * 100

avg_salary = df["MonthlyIncome"].mean()

avg_age = df["Age"].mean()

avg_experience = df["TotalWorkingYears"].mean()

row1 = st.columns(6)

row1[0].metric(
    "Employees",
    employees
)

row1[1].metric(
    "Employees Left",
    employees_left
)

row1[2].metric(
    "Employees Stayed",
    employees_stayed
)

row1[3].metric(
    "Attrition %",
    f"{attrition_rate:.2f}%"
)

row1[4].metric(
    "Average Age",
    f"{avg_age:.1f}"
)

row1[5].metric(
    "Average Salary",
    f"${avg_salary:.0f}"
)

st.markdown("---")

# ======================================================
# CHARTS
# ======================================================

left, right = st.columns(2)

with left:

    fig = px.pie(

        df,

        names="Attrition",

        title="Employee Attrition"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.histogram(

        df,

        x="Department",

        color="Attrition",

        title="Department-wise Attrition"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

left, right = st.columns(2)

with left:

    fig = px.box(

        df,

        x="Attrition",

        y="MonthlyIncome",

        color="Attrition",

        title="Salary Distribution"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.histogram(

        df,

        x="Age",

        color="Attrition",

        nbins=20,

        title="Age Distribution"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

st.subheader("Dataset Preview")

st.dataframe(
    df,
    use_container_width=True
)
st.markdown("---")

st.header("Executive AI Insights")

insights, recommendations = generate_insights(df)

for item in insights:

    st.info(item)

st.markdown("---")

st.header("Recommended HR Actions")

for item in recommendations:

    st.success(item)