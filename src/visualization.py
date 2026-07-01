import matplotlib.pyplot as plt
import pandas as pd


def plot_accuracy_comparison(csv_file):

    df = pd.read_csv(csv_file)

    df = df.sort_values(
        by="Accuracy",
        ascending=False
    )

    plt.figure(figsize=(10,6))

    plt.bar(
        df["Model"],
        df["Accuracy"]
    )

    plt.title("Model Accuracy Comparison")

    plt.ylabel("Accuracy")

    plt.xticks(rotation=25)

    plt.tight_layout()

    plt.savefig(
        "results/accuracy_comparison.png",
        dpi=300
    )

    plt.close()

    print("Accuracy Comparison Chart Saved")