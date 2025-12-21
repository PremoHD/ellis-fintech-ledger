from core.risk_governor import approve
from skills.web_research import run as web_research

SKILL_MAP = {}

SKILL_MAP["web_research"] = web_research


def execute(skill_name, *args, **kwargs):
    if skill_name not in SKILL_MAP:
        raise Exception(f"Unknown skill: {skill_name}")

    approve(0.2)
    return SKILL_MAP[skill_name](*args, **kwargs)