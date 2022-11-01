from subprocess import Popen, PIPE, STDOUT
from event import Event
import json

def dispatcher(event_json):
    event = Event(event_json)
    print(event.name())
    print(event.logs())
    print("\n\n")

def main():
    docker_events = "docker events --filter event=die --format '{{json .}}'"
    process = Popen(docker_events, shell=True, stdout=PIPE, stderr=STDOUT)

    with process.stdout:
        for line in iter(process.stdout.readline, b''):
            json_string = line.decode("utf-8").strip()
            dispatcher(json.loads(json_string))


if __name__ == "__main__":
    main()
