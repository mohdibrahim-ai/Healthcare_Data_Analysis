import pandas as pd
import matplotlib.pyplot as plt

print("Healthcare Data Analysis Project Started")

# Load healthcare dataset
df = pd.read_csv("healthcare_dataset.csv")

print("Dataset loaded successfully!")
print(df.head())

# Basic dataset overview

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Statistical summary of numerical columns

print("\nStatistical Summary:")
print(df.describe())

# Unique values in categorical columns

print("\nUnique Values:")
for column in df.select_dtypes(include="object").columns:
    print(column, ":", df[column].nunique())

    # Data Quality Report

print("\n===== DATA QUALITY REPORT =====")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nMissing Values:")
print(df.isnull().sum().to_string())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nNumerical Summary:")
print(df.describe().round(2))

# Create a cleaned copy of the dataset
df_clean = df.copy()

# Remove exact duplicate rows
df_clean = df_clean.drop_duplicates()

print("\n===== CLEANED DATASET =====")
print("Original rows:", len(df))
print("Rows after removing duplicates:", len(df_clean))
print("Duplicates removed:", len(df) - len(df_clean))

#  Analysis 1: Patients by medical condition 

condition_counts = df_clean["Medical Condition"].value_counts()

print(condition_counts)

condition_counts.plot(kind="bar", figsize=(8, 5))

plt.title("Number of Patients by Medical Condition")
plt.xlabel("Medical Condition")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

#  Analysis 2: Average billing amount by medical condition 

avg_billing = df_clean.groupby("Medical Condition")["Billing Amount"].mean()

print(avg_billing)

avg_billing.plot(kind="bar", figsize=(8, 5))

plt.title("Average Billing Amount by Medical Condition")
plt.xlabel("Medical Condition")
plt.ylabel("Average Billing Amount")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

  # Analysis 3: Patients by admission type 

admission_counts = df_clean["Admission Type"].value_counts()

print(admission_counts)

admission_counts.plot(kind="bar", figsize=(7, 5))

plt.title("Number of Patients by Admission Type")
plt.xlabel("Admission Type")
plt.ylabel("Number of Patients")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Analysis 4: Average Age by Medical Condition

avg_age = df_clean.groupby("Medical Condition")["Age"].mean()

print("\nAverage Age by Medical Condition:")
print(avg_age.round(2))

avg_age.plot(kind="bar", figsize=(8, 5))

plt.title("Average Age by Medical Condition")
plt.xlabel("Medical Condition")
plt.ylabel("Average Age")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()