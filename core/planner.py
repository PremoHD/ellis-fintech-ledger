from core.brain_profile import BrainProfile

def plan(task):
    if BrainProfile["speed_over_perfection"]:
        return ["analyze", "execute", "optimize"]
    return ["research", "design", "build", "test", "optimize"]