import re
import IntruAlert.config.settings as settings
from scapy.all import sniff
from IntruAlert.scripts.alert_system import log_alert

def packet_callback(packet):
    """
    This function will be called for every packet sniffed.
    """
    if packet.haslayer('TCP') or packet.haslayer('UDP'):
        # Convert packet to string to check against patterns
        packet_str = str(packet)
        check_for_suspicious_activities(packet_str)

def check_for_suspicious_activities(packet_str):
    # Instead of using config.settings, directly reference 'settings'
    with open(settings.SUSPICIOUS_PATTERNS_FILE, 'r') as file:
        patterns = file.readlines()

    for pattern in patterns:
        if re.search(pattern.strip(), packet_str):
            log_alert(f"Suspicious activity detected: {pattern.strip()}")

def start_network_monitor():
    """
    Start the network monitoring process.
    """
    sniff(prn=packet_callback, store=False)
