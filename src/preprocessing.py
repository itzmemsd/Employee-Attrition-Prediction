import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def load_data(file_path):
    """
    Load the employee attrition dataset.
    """
    return pd.read_csv(file_path)


def prepare_data(df):
    """
    Separate features and target.
    """

    drop_columns = [
        "EmployeeCount",
        "EmployeeNumber",
        "Over18",
        "StandardHours"
    ]

    df = df.drop(columns=drop_columns)

    # Encode target
    df["Attrition"] = df["Attrition"].map({
        "Yes": 1,
        "No": 0
    })

    X = df.drop("Attrition", axis=1)
    y = df["Attrition"]

    return X, y


def create_preprocessor(X):

    categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

    numerical_features = X.select_dtypes(exclude=["object"]).columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                StandardScaler(),
                numerical_features
            ),
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features
            )
        ]
    )

    return preprocessor