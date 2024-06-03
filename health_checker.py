import requests
import logging
import time

# Configuration
URL = "http://your-application-url.com"
CHECK_INTERVAL = 60  # in seconds
LOG_FILE = "application_health.log"

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(message, level="info"):
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    print(message)

def check_application_health():
    try:
        response = requests.get(URL, timeout=10)
        if response.status_code == 200:
            log_message(f"Application is UP. Status code: {response.status_code}")
        else:
            log_message(f"Application is DOWN. Status code: {response.status_code}", level="warning")
    except requests.exceptions.RequestException as e:
        log_message(f"Application is DOWN. Error: {str(e)}", level="error")

def monitor_application():
    log_message("Starting application health monitoring")
    while True:
        check_application_health()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_application()
