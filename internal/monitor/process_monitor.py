import psutil
from internal.collector.event_collector import collect_event

def monitor_processes():

    for proc in psutil.process_iter(['pid','name']):
        event = f"Process Started: {proc.info['name']}"
        collect_event(event)
