class Task:
    def __init__(self, intent, priority=1, online=False):
        self.intent = intent
        self.priority = priority
        self.online = online