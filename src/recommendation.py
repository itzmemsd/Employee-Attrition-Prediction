def generate_recommendation(probability, employee):

    recommendations = []

    if probability >= 0.70:

        risk = "HIGH"

    elif probability >= 0.40:

        risk = "MEDIUM"

    else:

        risk = "LOW"

    if employee["OverTime"].iloc[0] == "Yes":
        recommendations.append(
            "Reduce overtime workload."
        )

    if employee["JobSatisfaction"].iloc[0] <= 2:
        recommendations.append(
            "Improve job satisfaction through feedback sessions."
        )

    if employee["WorkLifeBalance"].iloc[0] <= 2:
        recommendations.append(
            "Provide flexible working arrangements."
        )

    if employee["DistanceFromHome"].iloc[0] >= 20:
        recommendations.append(
            "Consider hybrid or remote work options."
        )

    if employee["MonthlyIncome"].iloc[0] < 4000:
        recommendations.append(
            "Review compensation and benefits."
        )

    if employee["YearsSinceLastPromotion"].iloc[0] >= 5:
        recommendations.append(
            "Review promotion and career growth opportunities."
        )

    if not recommendations:
        recommendations.append(
            "No immediate HR intervention required."
        )

    return risk, recommendations