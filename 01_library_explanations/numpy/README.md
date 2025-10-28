# 2. numpy

The engine behind numerical calculations.

What it does:

Works with large sets of numbers efficiently.
pandas actually uses numpy underneath.

You’ll use it to:

• Perform mathematical operations

• Handle arrays (grids of numbers)

• Compute averages, medians, and matrix operations


Example:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(np.mean(arr))
