from subprocess import run

class Event:
    def __init__(self, json_event):
        self.json_event = json_event

    def time(self):
        return self.json_event["time"]

    def name(self):
        return self.json_event["Actor"]["Attributes"]["name"]

    def id(self):
        return self.json_event["id"]

    def logs(self):
        command = [
            "docker",
            "logs",
            "--since",
            f"{self.time() - 2}",
            f"{self.id()}"
        ]
        out = run(command, capture_output=True, text=True)
        return out.stderr
