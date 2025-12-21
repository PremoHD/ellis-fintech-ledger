from core.cooldown import allow

if allow("background_monitor", 300):
    agent.interrupt_and_execute(
        "monitor allowed resources and note changes"
    )