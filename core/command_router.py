from core.executive_agent import ExecutiveAgent

class CommandRouter:
    def __init__(self):
        self.agent = ExecutiveAgent()

    def handle(self, command: str):
        self.agent.interrupt_and_execute(command)