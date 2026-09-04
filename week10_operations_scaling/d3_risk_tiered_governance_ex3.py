# Risk-tiered AI governance demo.
# Classifies each task as high- or low-risk, audit-logs every decision, and
# routes high-risk outputs (e.g. credit decisions, medical advice) through a
# simulated human review step before they're returned.
def classify_risk(task):
    if task in ["credit_decision", "medical_advice"]:
        return "high-risk"
    return "low-risk"

def log_decision(task, output):
    print(f"[AUDIT LOG] Task: {task} | Output: {output}")

def human_review(output):
    print("Human review required")
    return f"Approved: {output}"

def ai_pipeline(task, input_data):

    risk = classify_risk(task)
    output = f"AI result for {input_data}"

    log_decision(task, output)

    if risk == "high-risk":
        output = human_review(output)

    return output


# Simulated tasks
print(ai_pipeline("recommendation", "product list"))
print(ai_pipeline("credit_decision", "loan application"))