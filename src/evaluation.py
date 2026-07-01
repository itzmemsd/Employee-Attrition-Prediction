import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    RocCurveDisplay
)

from sklearn.model_selection import cross_val_score


# ============================================================
# Evaluate Model
# ============================================================

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]

    metrics = {

        "Accuracy": accuracy_score(
            y_test,
            predictions
        ),

        "Precision": precision_score(
            y_test,
            predictions,
            zero_division=0
        ),

        "Recall": recall_score(
            y_test,
            predictions,
            zero_division=0
        ),

        "F1 Score": f1_score(
            y_test,
            predictions,
            zero_division=0
        ),

        "ROC AUC": roc_auc_score(
            y_test,
            probabilities
        ),

        "Confusion Matrix": confusion_matrix(
            y_test,
            predictions
        ),

        "Classification Report": classification_report(
            y_test,
            predictions
        )

    }

    return metrics


# ============================================================
# Cross Validation
# ============================================================

def cross_validate_model(model, X, y):

    scores = cross_val_score(
        model,
        X,
        y,
        cv=5,
        scoring="accuracy",
        n_jobs=-1
    )

    return scores.mean(), scores.std()


# ============================================================
# Save Confusion Matrix
# ============================================================

def save_confusion_matrix(cm):

    plt.figure(figsize=(6, 5))

    plt.imshow(cm, cmap="Blues")

    plt.title("Confusion Matrix")

    plt.xlabel("Predicted Label")

    plt.ylabel("Actual Label")

    plt.colorbar()

    for i in range(len(cm)):
        for j in range(len(cm)):
            plt.text(
                j,
                i,
                cm[i][j],
                ha="center",
                va="center",
                fontsize=12
            )

    plt.tight_layout()

    plt.savefig(
        "results/confusion_matrix.png",
        dpi=300
    )

    plt.close()


# ============================================================
# Save ROC Curve
# ============================================================

def save_roc_curve(model, X_test, y_test):

    RocCurveDisplay.from_estimator(
        model,
        X_test,
        y_test
    )

    plt.title("ROC Curve")

    plt.tight_layout()

    plt.savefig(
        "results/roc_curve.png",
        dpi=300
    )

    plt.close()