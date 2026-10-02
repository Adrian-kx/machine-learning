import matplotlib
import matplotlib.pyplot as plt
import numpy as np

categories = ["A", "B", "C", "D"]
values = [3, 7, 2, 5]
plt.bar(categories, values, width=0.5)
plt.title("Gráfico de Barras Simples")

plt.show()
