# This demo show a simple example of how multiple agents can disagree on the outcome of a task 
def agent_a(x):
    return x * 2

def agent_b(x):
    return x * 2.0001 # slightly diffrent result to simulate disagreement

answers = {"A": agent_a(10), "B": agent_b(10)}
print(answers)