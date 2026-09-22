import pandas
import numpy
import seaborn
import matplotlib.pyplot
import plotly.express
from MachineLearning.functions.logs import log_separator

base = pandas.read_csv("MachineLearning/data/credit_risk_dataset.csv")
base_credit = (
    base
    .rename(columns={
        "loan_amnt": "loan",
        "person_age": "age",
        "person_income": "income",
        "cb_person_default_on_file": "default"
    })
    [["loan", "age", "income", "default"]]
)

print(base_credit)
log_separator()
print(base_credit.head())
log_separator()
print(base_credit.tail())
log_separator()
print(base_credit.describe())
log_separator()
print(base_credit[base_credit['person_income'] >= 6])