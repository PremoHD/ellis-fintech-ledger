def execute(skill_name, *args, **kwargs):
    # Allow single skill or list of skills
    if isinstance(skill_name, list):
        results = []
        for skill in skill_name:
            results.append(execute(skill, *args, **kwargs))
        return results

    if skill_name not in SKILL_MAP:
        raise Exception(f"Unknown skill: {skill_name}")

    approve(0.2)
    return SKILL_MAP[skill_name](*args, **kwargs)