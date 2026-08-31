# SLO monitoring demo.
# Simulates a stream of requests with random latency/success outcomes,
# tracks running average latency and uptime, and flags an SLO violation
# whenever either metric crosses its target threshold.
import random

SLO_LATENCY = 1.5   # seconds
SLO_UPTIME = 0.99

latencies = []
uptime_events = []

for step in range(20):

    latency = random.uniform(0.5, 2.0)
    success = random.random() > 0.05

    latencies.append(latency)
    uptime_events.append(success)

    avg_latency = sum(latencies) / len(latencies)
    uptime = sum(uptime_events) / len(uptime_events)

    print(f"Step {step} | Latency: {latency:.2f}s | Success: {success}")

    if avg_latency > SLO_LATENCY:
        print("⚠ SLO Violation: Latency exceeded")

    if uptime < SLO_UPTIME:
        print("⚠ SLO Violation: Uptime below target")