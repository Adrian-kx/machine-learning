import pandas
import numpy
import seaborn
import matplotlib.pyplot
import plotly.express
from MachineLearning.functions.logs import log_separator
from .preload_data import base_credit

print(base_credit)
log_separator()
print(base_credit.head())
log_separator()
print(base_credit.tail())
log_separator()
print(base_credit.describe())
log_separator()
print(base_credit[base_credit['income'] >= 200000])