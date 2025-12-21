from core.executor import execute
from core.log import log


class ExecutiveAgent:
    def interrupt_and_execute(self, intent: str):
        log(f"Executing intent: {intent}")

        # TEMP: single-skill mapping (stable)
        if "monitor" in intent or "research" in intent:
            return execute("web_research", "https://github.com")

        log("No matching skill for intent")
        return None