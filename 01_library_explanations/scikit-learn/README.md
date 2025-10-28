🧪 5. scikit-learn (sklearn)

The main library for machine learning and data modeling.

What it does:

Gives you tools to train predictive models — e.g. regression, classification, clustering.

You’ll use it to:

• Train models that predict outcomes (e.g., student test scores)

• Split data into training/testing sets

• Evaluate model performance

Example:

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

X = df[['reading score', 'writing score']]

y = df['math score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()

model.fit(X_train, y_train)

print(model.score(X_test, y_test))
