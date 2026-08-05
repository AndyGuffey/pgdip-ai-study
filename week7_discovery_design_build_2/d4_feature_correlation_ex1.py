# Computes Pearson correlation between each feature (income, debt) and a
# binary loan-approval outcome in a tiny hand-built dataset, using
# pandas' corr().
# Learning purpose: understand correlation analysis as a first step in
# model explainability/fairness review — spotting which features are
# most associated with an outcome before checking a model for bias
# (e.g. proxy discrimination via a correlated feature).

import pandas as pd

data = pd.DataFrame({
    "income": [30, 50, 80, 40, 90],
    "debt": [10, 20, 10, 30, 5],
    "approved": [0, 1, 1, 0, 1]
})

correlations = data.corr()["approved"]
print(correlations)