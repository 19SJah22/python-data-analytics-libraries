//Load data

df = pd.read_csv("data.csv")

//View first rows

df.head()

//Get info about the dataset

df.info()

//Describe numerical columns

df.describe()

//Handle missing values

df = df.dropna() # remove missing rows

df = df.fillna(0) # replace missing with 0

//Filter and sort data

df_filtered = df[df["age"] > 25]

df_sorted = df.sort_values(by="salary", ascending=False)

//Group and summarize

avg_salary = df.groupby("department")["salary"].mean()

//Save cleaned data

df.to_csv("cleaned_data.csv", index=False)
