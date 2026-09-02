# Severity-classified incident response demo.
# Builds on the basic runbook pattern: classifies each detected incident into
# a severity tier (MINOR/MAJOR/CRITICAL) based on latency and error signals,
# applies a severity-appropriate recovery action, then runs a post-recovery
# health check to confirm the system actually recovered.
import random
import time

def system_health():
    """
    Simulate system health:
    - latency in seconds
    - error flag (True = error detected)
    """
    latency = random.uniform(0.5, 3.0)
    error = random.random() < 0.2
    return latency, error

def classify_incident(latency, error):
    """
    Simple severity classification based on latency and errors.
    """
    if error and latency > 2.5:
        return "CRITICAL"
    if error or latency > 2.0:
        return "MAJOR"
    if latency > 1.5:
        return "MINOR"
    return "NONE"

def recover(severity):
    """
    Simulated recovery action based on incident severity.
    """
    if severity == "CRITICAL":
        print("Applying recovery: Restarting service and clearing caches...")
    elif severity == "MAJOR":
        print("Applying recovery: Restarting service...")
    elif severity == "MINOR":
        print("Applying recovery: Reducing load / throttling traffic...")
    else:
        print("No recovery needed.")

def post_recovery_check():
    """
    Quick post-recovery health check.
    """
    latency, error = system_health()
    print(f"Post-recovery check | Latency: {latency:.2f} | Error: {error}")
    if not error and latency <= 2.0:
        print("Recovery validated: system healthy.\n")
    else:
        print("Recovery incomplete: further investigation needed.\n")

incident_count = 0

for step in range(12):
    latency, error = system_health()
    print(f"Step {step} | Latency: {latency:.2f} | Error: {error}")

    severity = classify_incident(latency, error)

    if severity != "NONE":
        incident_count += 1
        print(f"⚠ Incident detected (severity={severity}) → Starting response")
        recover(severity)
        time.sleep(0.2)  # simulate time taken to execute recovery
        print("Validating recovery...")
        post_recovery_check()
    else:
        print("System OK.\n")

print(f"Total incidents handled: {incident_count}")