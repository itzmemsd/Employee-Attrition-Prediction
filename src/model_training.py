from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier


def get_models(preprocessor):

    models = {

        "Logistic Regression":

        Pipeline([
            ("preprocessor", preprocessor),
            ("smote", SMOTE(random_state=42)),
            ("classifier",
                LogisticRegression(
                    max_iter=1000,
                    random_state=42
                ))
        ]),

        "Decision Tree":

        Pipeline([
            ("preprocessor", preprocessor),
            ("smote", SMOTE(random_state=42)),
            ("classifier",
                DecisionTreeClassifier(
                    random_state=42
                ))
        ]),

        "Random Forest":

        Pipeline([
            ("preprocessor", preprocessor),
            ("smote", SMOTE(random_state=42)),
            ("classifier",
                RandomForestClassifier(
                    n_estimators=300,
                    random_state=42,
                    n_jobs=-1
                ))
        ]),

        "Support Vector Machine":

        Pipeline([
            ("preprocessor", preprocessor),
            ("smote", SMOTE(random_state=42)),
            ("classifier",
                SVC(
                    kernel="rbf",
                    probability=True,
                    random_state=42
                ))
        ]),

        "XGBoost":

        Pipeline([
            ("preprocessor", preprocessor),
            ("smote", SMOTE(random_state=42)),
            ("classifier",
                XGBClassifier(
                    n_estimators=300,
                    learning_rate=0.05,
                    max_depth=6,
                    subsample=0.8,
                    colsample_bytree=0.8,
                    random_state=42,
                    eval_metric="logloss",
                    verbosity=0
                ))
        ]),

        "LightGBM":

        Pipeline([
            ("preprocessor", preprocessor),
            ("smote", SMOTE(random_state=42)),
            ("classifier",
                LGBMClassifier(
                    n_estimators=300,
                    learning_rate=0.05,
                    random_state=42,
                    verbose=-1
                ))
        ]),

        "CatBoost":

        Pipeline([
            ("preprocessor", preprocessor),
            ("smote", SMOTE(random_state=42)),
            ("classifier",
                CatBoostClassifier(
                    iterations=300,
                    learning_rate=0.05,
                    depth=6,
                    random_state=42,
                    verbose=False
                ))
        ])

    }

    return models