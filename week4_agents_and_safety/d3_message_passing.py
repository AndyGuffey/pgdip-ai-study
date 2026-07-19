# Small demo to show how message passing can be used to orchestrate multiple agents (Planner, Executor, Verifier) in a pipeline.

def planner_task(query):
    return f"PLAN: Break down the task '{query}' into steps"

def executor_task(step):
    return f"EXECUTE: Performing step '{step}'"

def verifier_task(execution_result):
    return f"VERIFY: Checking result of '{execution_result}'"

query = "Find the weather in Auckland and summarise it"

plan = planner_task(query)
execution_result = executor_task(plan)
verification_result = verifier_task(execution_result)

print(plan)
print(execution_result)
print(verification_result)