import time
from core.executive_agent import ExecutiveAgent
from core.kill_switch import is_active
from core.cooldown import allow


def run():
    agent = ExecutiveAgent()

    while is_active():
        if allow("background_tick", 300):
            agent.interrupt_and_execute(
                "monitor allowed resources and optimize if needed"
            )
        time.sleep(1)