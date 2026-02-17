from internal.monitor.process_monitor import monitor_processes
from internal.monitor.file_monitor import monitor_files
from internal.monitor.network_monitor import monitor_connections

print("[AegisEDR] Endpoint Monitoring Started")

monitor_processes()
monitor_files()
monitor_connections()
