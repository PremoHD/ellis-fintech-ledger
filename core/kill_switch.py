ACTIVE = True

def kill():
    global ACTIVE
    ACTIVE = False
    print("🛑 AGENT OFFLINE")

def is_active():
    return ACTIVE