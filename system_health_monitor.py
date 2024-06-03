import psutil
import logging
from datetime import datetime

# Set thresholds
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
DISK_THRESHOLD = 80.0

# Configure logging
logging.basicConfig(filename="system_health.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_alert(message):
    print(message)
    logging.info(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"ALERT: CPU usage is {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"ALERT: Memory usage is {memory_usage}%")

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"ALERT: Disk usage is {disk_usage}%")

def check_running_processes():
    processes = psutil.pids()
    if len(processes) > 500:  # Example threshold for the number of processes
        log_alert(f"ALERT: Number of running processes is {len(processes)}")

def monitor_system():
    log_alert("Starting system health monitoring")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    log_alert("Completed system health check")

if __name__ == "__main__":
    monitor_system()
