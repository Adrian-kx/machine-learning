import pandas as pd
from functions.change_value import change_values
from functions.logs import log_separator
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data/reviews.csv")

log_separator()
print(data.isnull().sum())
log_separator()
print(data.describe().round(2))

data = change_values(data)

log_separator()
print(data.isnull().sum())
log_separator()
print(data.describe().round(2))


log_separator()
