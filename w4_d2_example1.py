# Minimal example of agent state/memory: a simple key-value store an
# agent can write to (remember) and read from (recall) across a session,
# instead of relying only on what's in the current prompt/context.
class AgentState:
    def __init__(self):
        self.memory = {}

    def remember(self, key, value):
        self.memory[key] = value

    def recall(self, key):
        return self.memory.get(key)

state = AgentState()
state.remember("preferred_city", "Auckland")
print(state.recall("yes"))