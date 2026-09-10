import pandas as pd
import numpy as np

df = pd.read_excel("student_scores.xlsx")

math_scores = df['math_score'].to_numpy()

print("===== NUMPY OPERATIONS =====")

print("Mean:", np.nanmean(math_scores))
print("Median:", np.nanmedian(math_scores))
print("Maximum:", np.nanmax(math_scores))
print("Minimum:", np.nanmin(math_scores))

normalized_scores = (
    (math_scores - np.nanmin(math_scores))
    / (np.nanmax(math_scores) - np.nanmin(math_scores))
)

print("\nNormalized Scores:")
print(normalized_scores)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== ATTENDANCE BELOW 70% =====")
print(df[df['attendance'] < 70])

df['age'] = pd.to_numeric(df['age'], errors='coerce')

df['exam_date'] = pd.to_datetime(
    df['exam_date'],
    errors='coerce'
)

numeric_cols = [
    'age',
    'math_score',
    'science_score',
    'attendance'
]

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

categorical_cols = ['name', 'gender']

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

for col in ['math_score', 'science_score']:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)

    df[col] = df[col].clip(
        lower_limit,
        upper_limit
    )

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

df['average_score'] = (
    df['math_score'] +
    df['science_score']
) / 2

print("\n===== TOP 5 STUDENTS =====")

print(
    df.nlargest(
        5,
        'average_score'
    )[['name', 'average_score']]
)

correlation = df['attendance'].corr(
    df['average_score']
)

print("\nCorrelation Between Attendance and Marks:")
print(correlation)

print("\n===== AVERAGE MARKS BY GENDER =====")

print(
    df.groupby('gender')[
        [
            'math_score',
            'science_score',
            'average_score'
        ]
    ].mean()
)

df.to_csv(
    "cleaned_dataset.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")
