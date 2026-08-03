# Classifies a use case as HIGH_RISK or LOW_RISK using a single hardcoded
# list of high-risk domains (medical, finance, education) — no other
# context is considered.
# Learning purpose: understand the simplest possible form of AI risk
# classification as a baseline before adding the contextual factors seen
# in week7_discovery_design_build_2/d1_contextual_risk_classification_ex2.py.

def classify_risk(use_case):
    high_risk = ["medical", "finance", "education"]
    if use_case.lower() in high_risk:
        return "HIGH_RISK"
    return "LOW_RISK"

systems = ["spam filter", "medical", "finance", "chatbot"]

for s in systems:
    print(s, "â†’", classify_risk(s))