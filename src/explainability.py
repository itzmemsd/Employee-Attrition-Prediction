import shap
import joblib
import matplotlib.pyplot as plt


class ExplainableAI:

    def __init__(self):

        self.model = joblib.load("models/best_model.pkl")

    def explain(self, employee):

        classifier = self.model.named_steps["classifier"]

        preprocessor = self.model.named_steps["preprocessor"]

        X = preprocessor.transform(employee)

        explainer = shap.TreeExplainer(classifier)

        shap_values = explainer.shap_values(X)

        return explainer, shap_values, X

    def save_summary_plot(self, employee):

        explainer, shap_values, X = self.explain(employee)

        plt.figure()

        shap.summary_plot(
            shap_values,
            X,
            show=False
        )

        plt.tight_layout()

        plt.savefig(
            "results/shap_summary.png",
            dpi=300
        )

        plt.close()