from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(x, np.array([1, 2])) + 3

model = LinearRegression()

model.fit(x, y)

print("Coeficiente: ", model.coef_)
print("Intercept: ", model.intercept_)
