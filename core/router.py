from core.kill_switch import kill
from core.executor import execute


class Router:
    def handle(self, command: str):
        cmd = command.strip().lower()

        if cmd in ["go offline", "shutdown", "stop"]:
            kill()
            return

        if cmd.startswith("research "):
            url = command.split(" ", 1)[1]
            result = execute("web_research", url)
            print(result[:500])
            return

        print(f"⚠️ Unknown command: {command}")


router = Router() 