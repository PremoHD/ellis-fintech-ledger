import time

LAST_RUN = {}

def allow(task, cooldown=300):
    now = time.time()
    last = LAST_RUN.get(task, 0)
    if now - last >= cooldown:
        LAST_RUN[task] = now
        return True
    return False