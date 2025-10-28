# 3. matplotlib

The basic plotting and visualization library.

What it does:

Lets you create all kinds of charts and graphs (line, bar, pie, scatter, etc.).

You’ll use it to:

• Visualize your data clearly

• Customize graphs (titles, labels, colors)

• Save plots as images for reports


Example:

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [10, 20, 25, 30])

plt.title("Simple Line Chart")

plt.xlabel("X values")

plt.ylabel("Y values")

plt.show()
