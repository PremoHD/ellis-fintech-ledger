from core.command_router import CommandRouter

if __name__ == "__main__":
    router = CommandRouter()
    while True:
        cmd = input(">> ")
        router.handle(cmd)