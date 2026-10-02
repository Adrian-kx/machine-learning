from sklearn.linear_model import LinearRegression
import numpy as np

x_train = [[0, 0], [1, 1], [2, 2]]
y_train = [0, 1, 2]

regressor = LinearRegression()

regressor.fit(x_train, y_train)

x_test = [[3, 3]]
y_pred = regressor.predict(x_test)

print(y_pred)
