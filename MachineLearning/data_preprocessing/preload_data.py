import pandas

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