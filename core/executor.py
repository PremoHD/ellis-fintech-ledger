from skills.web_research import research

SKILL_MAP = {
    "web_research": research
}

def execute(skill_name, *args):
    if isinstance(skill_name, list):
        raise ValueError("Skill name must be a string, not a list")

    if skill_name not in SKILL_MAP:
        raise ValueError(f"Unknown skill: {skill_name}")

    return SKILL_MAP[skill_name](*args)