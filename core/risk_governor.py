import os

MAX_RISK = float(os.getenv("MAX_RISK", 0.7))

def approve(action_risk: float):
    if action_risk > MAX_RISK:
        raise Exception("❌ Risk Governor: Action exceeds allowed risk.")
    return True