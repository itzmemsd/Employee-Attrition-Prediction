import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split

from src.preprocessing import (
    load_data,
    prepare_data,
    create_preprocessor
)

from src.model_training import get_models

from src.evaluation import (
    evaluate_model,
    save_confusion_matrix,
    save_roc_curve
)

from src.visualization import (
    plot_accuracy_comparison
)

# ============================================================
# Create Required Directories
# ============================================================

os.makedirs("models", exist_ok=True)
os.makedirs("results", exist_ok=True)

print("=" * 70)
print("EMPLOYEE ATTRITION PREDICTION SYSTEM")
print("=" * 70)

# ============================================================
# Load Dataset
# ============================================================

df = load_data(
    "dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

print("\nDataset Loaded Successfully")
print("\nOriginal Shape :", df.shape)

# ============================================================
# Prepare Dataset
# ============================================================

X, y = prepare_data(df)

print("\nFeatures Shape :", X.shape)
print("Target Shape   :", y.shape)

# ============================================================
# Train Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ============================================================
# Create Preprocessor
# ============================================================

preprocessor = create_preprocessor(X)

# ============================================================
# Load Models
# ============================================================

models = get_models(preprocessor)

results = []

best_model = None
best_metrics = None
best_accuracy = 0

print("\n" + "=" * 70)
print("MODEL TRAINING")
print("=" * 70)

# ============================================================
# Train Models
# ============================================================

for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(X_train, y_train)

    metrics = evaluate_model(
        model,
        X_test,
        y_test
    )

    print(f"Accuracy  : {metrics['Accuracy']:.4f}")
    print(f"Precision : {metrics['Precision']:.4f}")
    print(f"Recall    : {metrics['Recall']:.4f}")
    print(f"F1 Score  : {metrics['F1 Score']:.4f}")
    print(f"ROC AUC   : {metrics['ROC AUC']:.4f}")

    results.append([
        name,
        metrics["Accuracy"],
        metrics["Precision"],
        metrics["Recall"],
        metrics["F1 Score"],
        metrics["ROC AUC"]
    ])

    if metrics["Accuracy"] > best_accuracy:
        best_accuracy = metrics["Accuracy"]
        best_model = model
        best_metrics = metrics

# ============================================================
# Model Comparison
# ============================================================

comparison = pd.DataFrame(
    results,
    columns=[
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC"
    ]
)

comparison = comparison.sort_values(
    by="Accuracy",
    ascending=False
)

comparison.to_csv(
    "results/model_comparison.csv",
    index=False
)

print("\n")
print("=" * 70)
print("MODEL COMPARISON")
print("=" * 70)

print(comparison)

# ============================================================
# Save Best Model
# ============================================================

joblib.dump(
    best_model,
    "models/best_model.pkl"
)

# ============================================================
# Save Classification Report
# ============================================================

with open(
    "results/classification_report.txt",
    "w"
) as file:

    file.write(
        best_metrics["Classification Report"]
    )

# ============================================================
# Save Confusion Matrix
# ============================================================

save_confusion_matrix(
    best_metrics["Confusion Matrix"]
)

# ============================================================
# Save ROC Curve
# ============================================================

save_roc_curve(
    best_model,
    X_test,
    y_test
)

# ============================================================
# Save Accuracy Comparison Chart
# ============================================================

plot_accuracy_comparison(
    "results/model_comparison.csv"
)

# ============================================================
# Final Output
# ============================================================

print("\nBest Model Saved Successfully")
print("Accuracy :", round(best_accuracy, 4))

print("\nGenerated Files")

print("✓ models/best_model.pkl")
print("✓ results/model_comparison.csv")
print("✓ results/classification_report.txt")
print("✓ results/confusion_matrix.png")
print("✓ results/roc_curve.png")
print("✓ results/accuracy_comparison.png")

print("\nPROJECT COMPLETED SUCCESSFULLY")