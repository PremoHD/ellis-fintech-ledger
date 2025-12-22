from core.executor import execute
from core.kill_switch import kill

class Router:
    def handle(self, command: str):
        cmd = command.strip().lower()

        if not cmd:
            return

        if cmd in ["go offline", "shutdown", "stop"]:
            kill()
            return

        if cmd == "help":
            print("Commands:")
            print("  research <url>")
            print("  go offline")
            return

        if cmd.startswith("research "):
            url = command.split(" ", 1)[1]
            result = execute("web_research", url)
            print(result[:500])
            return

        print("⚠️ Unknown command")

router = Router()