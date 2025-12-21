import time
from core.executive_agent import ExecutiveAgent
from core.kill_switch import is_active

def run():
    agent = ExecutiveAgent()
    while is_active():
        agent.interrupt_and_execute(
            "monitor allowed resources and optimize if needed"
        )
        time.sleep(300)  # every 5 minutes