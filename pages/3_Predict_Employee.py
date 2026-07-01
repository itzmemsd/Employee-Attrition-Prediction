from src.explainability import ExplainableAI
import streamlit as st
import joblib
import pandas as pd

from src.recommendation import generate_recommendation

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Employee Prediction",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Employee Attrition Prediction")

st.markdown(
    """
Predict the likelihood of an employee leaving the organization
using the trained XGBoost machine learning model.
"""
)

st.markdown("---")

# ============================================================
# LOAD MODEL
# ============================================================

try:

    model = joblib.load("models/best_model.pkl")

except Exception as e:

    st.error("Unable to load trained model.")

    st.exception(e)

    st.stop()

# ============================================================
# INPUT FORM
# ============================================================

st.subheader("Employee Information")

left, right = st.columns(2)

# ============================================================
# LEFT COLUMN
# ============================================================

with left:

    Age = st.slider(
        "Age",
        18,
        60,
        30
    )

    BusinessTravel = st.selectbox(

        "Business Travel",

        [

            "Non-Travel",

            "Travel_Rarely",

            "Travel_Frequently"

        ]

    )

    DailyRate = st.number_input(

        "Daily Rate",

        min_value=100,

        max_value=1600,

        value=800

    )

    Department = st.selectbox(

        "Department",

        [

            "Sales",

            "Research & Development",

            "Human Resources"

        ]

    )

    DistanceFromHome = st.slider(

        "Distance From Home",

        1,

        30,

        5

    )

    Education = st.selectbox(

        "Education",

        [

            1,

            2,

            3,

            4,

            5

        ]

    )

    EducationField = st.selectbox(

        "Education Field",

        [

            "Life Sciences",

            "Medical",

            "Marketing",

            "Technical Degree",

            "Human Resources",

            "Other"

        ]

    )

    EnvironmentSatisfaction = st.selectbox(

        "Environment Satisfaction",

        [

            1,

            2,

            3,

            4

        ]

    )

    Gender = st.selectbox(

        "Gender",

        [

            "Male",

            "Female"

        ]

    )

    HourlyRate = st.number_input(

        "Hourly Rate",

        min_value=20,

        max_value=120,

        value=60

    )

    JobInvolvement = st.selectbox(

        "Job Involvement",

        [

            1,

            2,

            3,

            4

        ]

    )

    JobLevel = st.selectbox(

        "Job Level",

        [

            1,

            2,

            3,

            4,

            5

        ]

    )

    JobRole = st.selectbox(

        "Job Role",

        [

            "Sales Executive",

            "Research Scientist",

            "Laboratory Technician",

            "Manufacturing Director",

            "Healthcare Representative",

            "Manager",

            "Sales Representative",

            "Research Director",

            "Human Resources"

        ]

    )

    JobSatisfaction = st.selectbox(

        "Job Satisfaction",

        [

            1,

            2,

            3,

            4

        ]

    )

    MaritalStatus = st.selectbox(

        "Marital Status",

        [

            "Single",

            "Married",

            "Divorced"

        ]

    )
    # ============================================================
# RIGHT COLUMN
# ============================================================

with right:

    MonthlyIncome = st.number_input(

        "Monthly Income",

        min_value=1000,

        max_value=50000,

        value=5000,

        step=100

    )

    MonthlyRate = st.number_input(

        "Monthly Rate",

        min_value=1000,

        max_value=30000,

        value=12000,

        step=100

    )

    NumCompaniesWorked = st.slider(

        "Number of Companies Worked",

        0,

        10,

        2

    )

    OverTime = st.selectbox(

        "OverTime",

        [

            "Yes",

            "No"

        ]

    )

    PercentSalaryHike = st.slider(

        "Percent Salary Hike",

        10,

        25,

        15

    )

    PerformanceRating = st.selectbox(

        "Performance Rating",

        [

            3,

            4

        ]

    )

    RelationshipSatisfaction = st.selectbox(

        "Relationship Satisfaction",

        [

            1,

            2,

            3,

            4

        ]

    )

    StockOptionLevel = st.selectbox(

        "Stock Option Level",

        [

            0,

            1,

            2,

            3

        ]

    )

    TotalWorkingYears = st.slider(

        "Total Working Years",

        0,

        40,

        10

    )

    TrainingTimesLastYear = st.slider(

        "Training Times Last Year",

        0,

        6,

        2

    )

    WorkLifeBalance = st.selectbox(

        "Work Life Balance",

        [

            1,

            2,

            3,

            4

        ]

    )

    YearsAtCompany = st.slider(

        "Years At Company",

        0,

        40,

        5

    )

    YearsInCurrentRole = st.slider(

        "Years In Current Role",

        0,

        20,

        3

    )

    YearsSinceLastPromotion = st.slider(

        "Years Since Last Promotion",

        0,

        15,

        1

    )

    YearsWithCurrManager = st.slider(

        "Years With Current Manager",

        0,

        20,

        3

    )

st.markdown("---")

predict = st.button(
    "🚀 Predict Employee Attrition",
    use_container_width=True
)

# ============================================================
# CREATE DATAFRAME
# ============================================================

if predict:

    employee = pd.DataFrame({

        "Age":[Age],

        "BusinessTravel":[BusinessTravel],

        "DailyRate":[DailyRate],

        "Department":[Department],

        "DistanceFromHome":[DistanceFromHome],

        "Education":[Education],

        "EducationField":[EducationField],

        "EnvironmentSatisfaction":[EnvironmentSatisfaction],

        "Gender":[Gender],

        "HourlyRate":[HourlyRate],

        "JobInvolvement":[JobInvolvement],

        "JobLevel":[JobLevel],

        "JobRole":[JobRole],

        "JobSatisfaction":[JobSatisfaction],

        "MaritalStatus":[MaritalStatus],

        "MonthlyIncome":[MonthlyIncome],

        "MonthlyRate":[MonthlyRate],

        "NumCompaniesWorked":[NumCompaniesWorked],

        "OverTime":[OverTime],

        "PercentSalaryHike":[PercentSalaryHike],

        "PerformanceRating":[PerformanceRating],

        "RelationshipSatisfaction":[RelationshipSatisfaction],

        "StockOptionLevel":[StockOptionLevel],

        "TotalWorkingYears":[TotalWorkingYears],

        "TrainingTimesLastYear":[TrainingTimesLastYear],

        "WorkLifeBalance":[WorkLifeBalance],

        "YearsAtCompany":[YearsAtCompany],

        "YearsInCurrentRole":[YearsInCurrentRole],

        "YearsSinceLastPromotion":[YearsSinceLastPromotion],

        "YearsWithCurrManager":[YearsWithCurrManager]

    })
        # ============================================================
    # MAKE PREDICTION
    # ============================================================

    try:

        prediction = model.predict(employee)[0]

        probability = model.predict_proba(employee)[0][1]

    except Exception as e:

        st.error("Prediction Failed")

        st.exception(e)

        st.stop()

    # ============================================================
    # AI RECOMMENDATION ENGINE
    # ============================================================

    risk, recommendations = generate_recommendation(
        probability,
        employee
    )

    st.markdown("---")

    st.header("Prediction Result")

    col1, col2, col3 = st.columns(3)

    # ============================================================
    # PREDICTION
    # ============================================================

    with col1:

        if prediction == 1:

            st.error("⚠ Employee Likely to Leave")

        else:

            st.success("✅ Employee Likely to Stay")

    # ============================================================
    # PROBABILITY
    # ============================================================

    with col2:

        st.metric(

            "Attrition Probability",

            f"{probability*100:.2f}%"

        )

    # ============================================================
    # RISK LEVEL
    # ============================================================

    with col3:

        if risk == "HIGH":

            st.error("🔴 HIGH RISK")

        elif risk == "MEDIUM":

            st.warning("🟡 MEDIUM RISK")

        else:

            st.success("🟢 LOW RISK")

    st.markdown("---")

    # ============================================================
    # HR RECOMMENDATIONS
    # ============================================================

    st.subheader("Recommended HR Actions")

    for item in recommendations:

        st.write("✔", item)

    st.markdown("---")

    # ============================================================
    # EMPLOYEE SUMMARY
    # ============================================================

    st.subheader("Employee Summary")

    summary = pd.DataFrame({

        "Feature": employee.columns,

        "Value": employee.iloc[0].values

    })

    st.dataframe(
        summary,
        use_container_width=True
    )
        # ============================================================
    # RISK GAUGE
    # ============================================================

    import plotly.graph_objects as go

    st.markdown("---")

    st.subheader("Attrition Risk Gauge")

    gauge = go.Figure(go.Indicator(

        mode="gauge+number",

        value=probability * 100,

        title={"text": "Risk Score (%)"},

        gauge={

            "axis": {"range": [0, 100]},

            "bar": {"color": "darkblue"},

            "steps": [

                {"range": [0, 40], "color": "lightgreen"},

                {"range": [40, 70], "color": "gold"},

                {"range": [70, 100], "color": "tomato"}

            ]

        }

    ))

    gauge.update_layout(height=400)

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    # ============================================================
    # DOWNLOAD RESULTS
    # ============================================================

    st.markdown("---")

    st.subheader("Download Prediction")

    result = pd.DataFrame({

        "Prediction": [
            "Likely to Leave" if prediction == 1
            else "Likely to Stay"
        ],

        "Probability (%)": [
            round(probability * 100, 2)
        ],

        "Risk Level": [
            risk
        ]

    })

    csv = result.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="📥 Download Prediction Report",

        data=csv,

        file_name="employee_attrition_prediction.csv",

        mime="text/csv"

    )

    # ============================================================
    # SUCCESS MESSAGE
    # ============================================================

    st.success(
        "Prediction completed successfully."
    )
st.markdown("---")

st.subheader("Explainable AI")

try:

    ai = ExplainableAI()

    ai.save_summary_plot(employee)

    st.image(
        "results/shap_summary.png"
    )

except Exception as e:

    st.warning(
        "Unable to generate SHAP explanation."
    )

    st.write(e)

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Employee Attrition Analytics & AI Decision Support System | "
    "Developed by Dr. M. Sasidharan"
)