import psutil
from internal.collector.event_collector import collect_event

def monitor_connections():

    for conn in psutil.net_connections():
        if conn.raddr:
            collect_event(f"Connection to {conn.raddr}")
