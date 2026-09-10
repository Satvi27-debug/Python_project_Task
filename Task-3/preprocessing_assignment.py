import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Load dataset
df = pd.read_excel("random_dataset.xlsx")

print("Shape:", df.shape)
print(df.head())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Handle outliers using IQR
for col in ["Age", "Salary", "Experience"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]

# One-Hot Encoding
df = pd.get_dummies(df, columns=["Department"], drop_first=True)

# Ordinal Encoding
perf_map = {"Low": 1, "Medium": 2, "High": 3}
df["Performance"] = df["Performance"].map(perf_map)

# Remove irrelevant feature
df = df.drop(columns=["EmployeeID"])

# Feature Scaling
scaler = StandardScaler()
num_cols = ["Age", "Salary", "Experience"]
df[num_cols] = scaler.fit_transform(df[num_cols])

# Handle skewness
df["Salary"] = np.sign(df["Salary"]) * np.log1p(np.abs(df["Salary"]))

# Save cleaned dataset
df.to_excel("cleaned_dataset.xlsx", index=False)

print("\nCleaned Dataset Shape:", df.shape)
print("Saved as cleaned_dataset.xlsx")
