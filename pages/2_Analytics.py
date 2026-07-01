import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="HR Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Employee Analytics Dashboard")

df = pd.read_csv(
    "dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

st.sidebar.header("Dashboard Filters")

department = st.sidebar.multiselect(
    "Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

gender = st.sidebar.multiselect(
    "Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

attrition = st.sidebar.multiselect(
    "Attrition",
    options=df["Attrition"].unique(),
    default=df["Attrition"].unique()
)

job_role = st.sidebar.multiselect(
    "Job Role",
    options=df["JobRole"].unique(),
    default=df["JobRole"].unique()
)

# ==========================================================
# FILTER DATASET
# ==========================================================

filtered_df = df[
    (df["Department"].isin(department)) &
    (df["Gender"].isin(gender)) &
    (df["Attrition"].isin(attrition)) &
    (df["JobRole"].isin(job_role))
]

# ==========================================================
# KPI SECTION
# ==========================================================

employees = len(filtered_df)

employees_left = len(
    filtered_df[
        filtered_df["Attrition"]=="Yes"
    ]
)

attrition_rate = 0

if employees > 0:
    attrition_rate = employees_left / employees * 100

avg_salary = filtered_df["MonthlyIncome"].mean()

avg_age = filtered_df["Age"].mean()

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Employees",
    employees
)

col2.metric(
    "Employees Left",
    employees_left
)

col3.metric(
    "Attrition %",
    f"{attrition_rate:.2f}%"
)

col4.metric(
    "Average Salary",
    f"${avg_salary:,.0f}"
)

st.markdown("---")

# ==========================================================
# FIRST ROW
# ==========================================================

left,right = st.columns(2)

with left:

    fig = px.histogram(
        filtered_df,
        x="Department",
        color="Attrition",
        title="Department-wise Attrition"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.histogram(
        filtered_df,
        x="Gender",
        color="Attrition",
        title="Gender Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# SECOND ROW
# ==========================================================

left,right = st.columns(2)

with left:

    fig = px.histogram(
        filtered_df,
        x="OverTime",
        color="Attrition",
        title="Overtime Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.box(
        filtered_df,
        x="Attrition",
        y="MonthlyIncome",
        color="Attrition",
        title="Salary Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# THIRD ROW
# ==========================================================

left,right = st.columns(2)

with left:

    fig = px.scatter(
        filtered_df,
        x="Age",
        y="MonthlyIncome",
        color="Attrition",
        title="Age vs Monthly Income"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.scatter(
        filtered_df,
        x="TotalWorkingYears",
        y="YearsAtCompany",
        color="Attrition",
        title="Experience vs Company Tenure"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

st.subheader("Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)