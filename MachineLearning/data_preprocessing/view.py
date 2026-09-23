import pandas
import numpy
import seaborn
import matplotlib.pyplot
import plotly.express
from .preload_data import base_credit


seaborn.countplot(data=base_credit, x="default")
grafico1 = matplotlib.pyplot

grafico2 = plotly.express.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color='age')

grafico2.show()
