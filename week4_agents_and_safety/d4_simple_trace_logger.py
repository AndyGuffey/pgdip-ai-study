# Agent observability/tracing: a minimal trace logger that stamps an event
# dict with the current time and appends it as a JSON line to trace.log,
# building up an on-disk, replayable record of an agent's decisions/actions.

import json, time

def log_event(event):
    event["timestamp"] = time.time()
    with open("trace.log","a") as f:
        f.write(json.dumps(event)+"\n")
