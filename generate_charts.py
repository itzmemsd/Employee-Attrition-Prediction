import os
import pandas as pd
import matplotlib.pyplot as plt
from src.preprocessing import load_data

# Create results folder
os.makedirs("results", exist_ok=True)

# Load dataset (original dataset without encoding)
df = load_data("dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv")

plt.style.use("ggplot")

print("=" * 70)
print("GENERATING EXPLORATORY DATA ANALYSIS CHARTS")
print("=" * 70)

# -------------------------------
# Figure 1 - Attrition Distribution
# -------------------------------
plt.figure(figsize=(6,5))
df["Attrition"].value_counts().plot(kind="bar")
plt.title("Employee Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("results/Figure_4_1_Attrition_Distribution.png")
plt.close()

print("✓ Figure 4.1 Generated")

# -------------------------------
# Figure 2 - Gender Distribution
# -------------------------------
plt.figure(figsize=(6,5))
df["Gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("results/Figure_4_2_Gender_Distribution.png")
plt.close()

print("✓ Figure 4.2 Generated")

# -------------------------------
# Figure 3 - Department Distribution
# -------------------------------
plt.figure(figsize=(7,5))
df["Department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("results/Figure_4_3_Department_Distribution.png")
plt.close()

print("✓ Figure 4.3 Generated")

# -------------------------------
# Figure 4 - Job Role Distribution
# -------------------------------
plt.figure(figsize=(10,5))
df["JobRole"].value_counts().plot(kind="bar")
plt.title("Job Role Distribution")
plt.xlabel("Job Role")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("results/Figure_4_4_JobRole_Distribution.png")
plt.close()

print("✓ Figure 4.4 Generated")

print("\nEDA Charts Generated Successfully!")