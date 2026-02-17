from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from internal.collector.event_collector import collect_event
import time

class Handler(FileSystemEventHandler):

    def on_created(self, event):
        collect_event(f"File Created: {event.src_path}")

def monitor_files():

    observer = Observer()
    observer.schedule(Handler(), path="/tmp", recursive=True)
    observer.start()
    time.sleep(5)
    observer.stop()
