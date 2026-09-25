from pathlib import Path
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

base_credit = pd.read_pickle(
    Path(__file__)
    .with_name("credit_risk_dataset.pkl")
    )

