import pandas as pd

print("=" * 70)
print("EMPLOYEE ATTRITION PREDICTION SYSTEM")
print("=" * 70)

# Load Dataset
df = pd.read_csv("dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv")

print("\n✅ Dataset Loaded Successfully")

# First Five Records
print("\nFirst Five Records")
print(df.head())

# Dataset Shape
print("\nDataset Shape")
print(df.shape)

# Column Names
print("\nColumn Names")
print(df.columns.tolist())

# Data Types
print("\nData Types")
print(df.dtypes)

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Duplicate Records
print("\nDuplicate Records")
print(df.duplicated().sum())

# Dataset Information
print("\nDataset Information")
df.info()

# Statistical Summary
print("\nStatistical Summary")
print(df.describe(include="all"))