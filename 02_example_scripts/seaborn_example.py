import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset
tips = sns.load_dataset("tips")

# Scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Bill vs Tip")
plt.show()

# Box plot
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Total Bill by Day")
plt.show()
