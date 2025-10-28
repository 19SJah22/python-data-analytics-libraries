# 6. plotly

Interactive and modern data visualizations.

What it does:

Creates charts you can zoom, hover, and explore in your browser or Jupyter Notebook.

You’ll use it to:

• Make interactive dashboards

• Build visual data stories for your portfolio

Example:

import plotly.express as px

fig = px.scatter(df, x="release_year", y="duration", color="type")

fig.show()
