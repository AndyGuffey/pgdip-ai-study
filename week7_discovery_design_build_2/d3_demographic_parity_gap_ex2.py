# Measures the demographic parity gap for loan approvals across two age
# groups — the raw difference between group approval rates, as an
# alternative to the ratio-based metric in
# week7_discovery_design_build_2/d3_disparity_ratio_ex1.py.
# Learning purpose: see how a difference-based fairness metric behaves
# differently from a ratio-based one on the same kind of data, and why
# there's more than one way to define "fair" approval rates.

import pandas as pd
# New example: loan approval by age_group
data = pd.DataFrame({
    # 50 young applicants, 50 senior applicants
    "age_group": ["young"] * 50 + ["senior"] * 50,
    # young: 40 approved, 10 rejected
    # senior: 25 approved, 25 rejected
    "approved": [1]*40 + [0]*10 + [1]*25 + [0]*25,
})

# Approval rate by age_group
approval_rates = data.groupby("age_group")["approved"].mean()
print("Approval rates by age_group:")
print(approval_rates)

# Demographic parity gap: difference in approval rates
parity_gap = approval_rates["young"] - approval_rates["senior"]
print("Demographic parity gap (young - senior):", parity_gap)