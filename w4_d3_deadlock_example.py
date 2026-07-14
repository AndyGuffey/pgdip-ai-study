# A simplified example of a deadlock situation where two agents are waiting for each other to release a resource

messages = [
    "Executor: Need clarification from Planner before proceeding.",
    "Planner: Waiting for Executor to finish before providing clarification.",
    "Verifier: Waiting for Executor to finish before verifying results."
]

if messages.count("Executor: Need clarification from Planner before proceeding.") > 1 and messages.count("Planner: Waiting for Executor to finish before providing clarification.") > 1:
    print("Deadlock detected breaking loop")