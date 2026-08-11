# Tool registry shape for enterprise-system actions (CRM lookup, ticketing)
# an agent could call, listing name/description/input schema with no
# execution logic wired up yet.
tool_registry = {
    "get_customer": {
        "description": "Fetch customer profile",
        "input_schema": {
            "customer_id": "string"
        }
    },
    "create_ticket": {
        "description": "Create a support ticket",
        "input_schema": {
            "title": "string",
            "priority": "low|medium|high"
        }
    }
}

def list_tools():
    return tool_registry.keys()

print("Available tools:", list_tools())