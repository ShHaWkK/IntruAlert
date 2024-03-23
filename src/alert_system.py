import time
import config.settings as settings

def log_alert(message):
    """
    Log an alert to the alerts log file.
    """
    with open(settings.ALERT_LOG_PATH, 'a') as log_file:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"[{timestamp}] ALERT: {message}\n")
