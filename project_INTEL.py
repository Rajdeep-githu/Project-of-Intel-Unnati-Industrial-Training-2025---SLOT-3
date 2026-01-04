# AXIOMFLOW - SIMPLE AI AGENT FRAMEWORK

# ---------- SDK (Framework Core) ----------

class Flow:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def task(self, name, component):
        self.tasks.append((name, component))
        return self

    def run(self, input_data):
        state = input_data
        print(f"\n▶ Running Flow: {self.name}")

        for name, component in self.tasks:
            print(f"\n➡ Executing task: {name}")
            state = component.execute(state)
            print(f"✔ Output: {state}")

        print("\n✅ Flow completed\n")
        return state


class Agent:
    def __init__(self, name):
        self.name = name

    def execute(self, state):
        plan = self.plan(state)
        decision = self.decide(plan)
        return decision

    def plan(self, state):
        raise NotImplementedError

    def decide(self, observation):
        raise NotImplementedError


class Tool:
    def execute(self, state):
        raise NotImplementedError


class MemoryStore:
    def __init__(self):
        self.data = {}

    def write(self, key, value):
        self.data[key] = value

    def read(self, key):
        return self.data.get(key)


# ---------- Observability ----------

def log(message):
    print(f"[LOG] {message}")


# ---------- Reference Agent 1: Document Intelligence ----------

class OCRTool(Tool):
    def execute(self, state):
        log("Running OCR Tool (simulated OpenVINO)")
        return {
            "text": "This is extracted document text",
            "confidence": 0.91
        }


document_flow = (
    Flow("Document Intelligence Flow")
    .task("OCR", OCRTool())
)


# ---------- Reference Agent 2: Support Resolver ----------

class RouterAgent(Agent):
    def plan(self, state):
        log("Planning route")
        return state["query"]

    def decide(self, observation):
        if "refund" in observation.lower():
            return {"route": "Billing Team", "confidence": 0.90}
        return {"route": "FAQ Bot", "confidence": 0.95}


class AgentWrapper:
    def __init__(self, agent):
        self.agent = agent

    def execute(self, state):
        return self.agent.execute(state)


support_flow = (
    Flow("Support Resolver Flow")
    .task("Route Ticket", AgentWrapper(RouterAgent("Router")))
)


# ---------- MAIN EXECUTION ----------

if __name__ == "__main__":

    print("\n==============================")
    print(" AXIOMFLOW FRAMEWORK DEMO ")
    print("==============================")

    # Run Document Intelligence Agent
    document_flow.run({"image": "sample_document.png"})

    # Run Support Resolver Agent
    support_flow.run({"query": "I want a refund for my order"})
