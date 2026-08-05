# Tests counterfactual fairness: runs the same rule-based decision model
# on a person's data, then on a counterfactual version where only the
# protected attribute (group) is changed, and compares the outcomes.
# Learning purpose: see counterfactual fairness as a complementary check
# to the aggregate metrics in
# week7_discovery_design_build_2/d3_disparity_ratio_ex1.py and
# d3_demographic_parity_gap_ex2.py — instead of comparing group
# statistics, it asks whether a single individual's outcome would change
# if only their group membership changed.

import pandas as pd

def model_decision(row):
    # simple rule-based "model"
    if row["income"] > 40000 and row["group"] == "A":
        return 1
    return 0

person = {"income": 50000, "group": "A"}
counterfactual = {"income": 50000, "group": "B"}

print("Original decision:", model_decision(person))
print("Counterfactual decision:", model_decision(counterfactual))