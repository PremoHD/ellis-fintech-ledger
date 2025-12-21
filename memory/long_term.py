import json

FILE = "memory/long_term.json"

def store_experience(data):
    try:
        with open(FILE, "r") as f:
            memory = json.load(f)
    except:
        memory = []

    memory.append(data)

    with open(FILE, "w") as f:
        json.dump(memory, f, indent=2)