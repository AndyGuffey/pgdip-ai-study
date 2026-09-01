# Incident response / runbook automation demo.
# Simulates system health checks (latency, error rate); when either crosses
# an alert threshold it runs a fixed remediation runbook, then escalates to
# a senior engineer if the incident isn't resolved.
import random

def check_system():
    latency = random.uniform(0.5, 3.0)
    error = random.random() < 0.2
    return latency, error

def runbook():
    print("Runbook Step 1: Check system health")
    print("Runbook Step 2: Restart service")
    print("Runbook Step 3: Verify recovery")

def escalate():
    print("Escalating to senior engineer...")

for step in range(10):

    latency, error = check_system()
    print(f"Step {step} | Latency: {latency:.2f} | Error: {error}")

    if latency > 2.0 or error:
        print("⚠ ALERT: Incident detected")
        runbook()

        resolved = random.random() > 0.5
        if not resolved:
            escalate()