from core.risk_governor import approve

def allow_online_action(purpose, risk=0.2):
    approve(risk)
    print(f"🌐 Online action approved: {purpose}")
    return True