from core.risk_governor import approve
from skills import analyze_system, automate_task, optimize_code

SKILL_MAP = {
    "analyze_system": analyze_system.run,
    "automate_task": automate_task.run,
    "optimize_code": optimize_code.run
}

def execute(skills):
    results = []
    for skill in skills:
        approve(0.3)
        results.append(SKILL_MAP[skill]())
    return results