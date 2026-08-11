# Mocks pulling structured data from an external system (a CRM) and
# folding it into an AI-facing summary string.
def crm_lookup(customer_id):
    return {"id": customer_id, "status": "gold", "region": "APAC"}

def ai_enriched_summary(customer_id):
    crm_data = crm_lookup(customer_id)
    return f"Customer {customer_id} is a {crm_data['status']} customer in {crm_data['region']}."