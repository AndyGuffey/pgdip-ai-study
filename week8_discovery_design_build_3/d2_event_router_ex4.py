# Routes an event to a handling team by type, complementing the queue-based
# worker in d2_event_queue_worker_ex3.py with a dispatch/routing step.
def route_event(event):
    if event["type"] == "payment_failed":
        return "finance_team"
    if event["type"] == "ticket_created":
        return "support_team"
    return "default_queue"

event = {"type": "ticket_created"}
print("Routed to:", route_event(event))