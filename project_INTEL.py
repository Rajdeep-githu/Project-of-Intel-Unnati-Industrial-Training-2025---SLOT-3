class Flow:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def task(self, name, component):
        self.tasks.append((name, component))
        return self
class Agent:
    def __init__(self, name):
        self.name = name

    def plan(self, state):
        raise NotImplementedError("Agent must implement plan()")

    def decide(self, observation):
        raise NotImplementedError("Agent must implement decide()")
class Tool:
    def execute(self, input_data, context):
        raise NotImplementedError("Tool must implement execute()")
class MemoryStore:
    def __init__(self):
        self.data = {}

    def read(self, key):
        return self.data.get(key)

    def write(self, key, value):
        self.data[key] = value
from sdk.flow import Flow
from sdk.agent import Agent

class TestAgent(Agent):
    def plan(self, state):
        return "plan"

    def decide(self, observation):
        return "decision"

flow = Flow("test_flow")
flow.task("test_task", TestAgent("agent1"))

print(flow.name)
print(flow.tasks)
