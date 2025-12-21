from core.planner import plan
from core.skill_selector import select_skills
from core.executor import execute
from core.evaluator import evaluate
from core.self_improver import improve
from memory.short_term import store_task

class ExecutiveAgent:
    def interrupt_and_execute(self, command):
        print("⚡ Interrupt received")
        store_task(command)

        steps = plan(command)
        skills = select_skills(steps)
        result = execute(skills)
        score = evaluate(result)
        improve(command, result, score)