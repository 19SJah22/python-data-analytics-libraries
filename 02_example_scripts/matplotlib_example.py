import matplotlib.pyplot as plt

# Basic line chart
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o', color='b')
plt.title("Simple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# Histogram
data = [10, 20, 20, 30, 40, 40, 40, 50, 60]
plt.hist(data, bins=5)
plt.title("Histogram Example")
plt.show()
