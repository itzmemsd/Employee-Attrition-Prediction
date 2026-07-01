import pandas as pd


def generate_insights(df):

    insights = []

    employees = len(df)

    left = len(df[df["Attrition"] == "Yes"])

    rate = left / employees * 100

    insights.append(
        f"Employee Attrition Rate : {rate:.2f}%"
    )

    dept = (
        df[df["Attrition"] == "Yes"]
        .groupby("Department")
        .size()
        .idxmax()
    )

    insights.append(
        f"Highest Attrition Department : {dept}"
    )

    overtime = (
        df[df["OverTime"] == "Yes"]["Attrition"]
        .value_counts()
    )

    if "Yes" in overtime.index:

        insights.append(
            "Employees working overtime show higher attrition."
        )

    avg_income = df["MonthlyIncome"].mean()

    insights.append(
        f"Average Monthly Income : ${avg_income:,.0f}"
    )

    avg_age = df["Age"].mean()

    insights.append(
        f"Average Employee Age : {avg_age:.1f} years"
    )

    recommendations = [

        "Reduce overtime wherever possible.",

        "Improve work-life balance initiatives.",

        "Conduct regular employee engagement surveys.",

        "Review salary and promotion policies.",

        "Provide career development opportunities."

    ]

    return insights, recommendations