import pandas as pd

# Load a CSV file (replace with your own)
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

# View first few rows
print(df.head())

# Select specific columns
age_gender = df[["age", "gender"]]
print(age_gender.head())

# Filter rows
adults = df[df["age"] > 18]
print(adults.head())

# Group and summarize
print(df.groupby("gender")["age"].mean())
