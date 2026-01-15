import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([100, 150, 200, 250, 300])

model = LinearRegression()
model.fit(X, y)
