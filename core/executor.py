from core.risk_governor import approve
from skills.web_research import run as web_research

SKILL_MAP = {
    "web_research": web_research
}


def execute(skill_name, *args, **kwargs):
    # HARD GUARD: only allow strings
    if not isinstance(skill_name, str):
        raise TypeError(f"execute() expects str, got {type(skill_name)}")

    if skill_name not in SKILL_MAP:
        raise Exception(f"Unknown skill: {skill_name}")

    approve(0.2)
    return SKILL_MAP[skill_name](*args, **kwargs)