# Event-driven integration pattern: an AI worker consumes events off a
# queue asynchronously instead of being called directly per request.
from queue import Queue

event_queue = Queue()

def publish_event(event):
    event_queue.put(event)

def ai_worker():
    while not event_queue.empty():
        event = event_queue.get()
        print(f"AI processing event: {event}")

publish_event({"type": "ticket_created", "priority": "high"})
publish_event({"type": "payment_failed"})

ai_worker()