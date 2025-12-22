from core.router import router

def main():
    print("✅ Agent online. Type 'help' or 'go offline'.")
    while True:
        try:
            cmd = input(">> ")
            router.handle(cmd)
        except KeyboardInterrupt:
            print("\n🛑 Exiting.")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()