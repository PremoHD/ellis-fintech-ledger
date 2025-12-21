def select_skills(steps):
    mapping = {
        "analyze": "analyze_system",
        "execute": "automate_task",
        "optimize": "optimize_code"
    }
    return [mapping[s] for s in steps if s in mapping]