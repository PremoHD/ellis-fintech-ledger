import threading
from core.background_loop import run as background_run
from core.router import router
from core.kill_switch import is_active

def interactive():
    while is_active():
        try:
            cmd = input(">> ").strip()
            if cmd:
                router.handle(cmd)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    t = threading.Thread(target=background_run, daemon=True)
    t.start()
    interactive()