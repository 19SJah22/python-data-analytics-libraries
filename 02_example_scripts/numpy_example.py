import numpy as np

# Create an array
arr = np.array([10, 20, 30, 40, 50])

# Basic stats
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

# Random numbers
rand_arr = np.random.randint(1, 100, 5)
print("Random numbers:", rand_arr)

# Reshape arrays
matrix = np.arange(1, 10).reshape(3, 3)
print("3x3 Matrix:\n", matrix)
