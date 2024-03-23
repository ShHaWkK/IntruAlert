from .network_monitor import start_network_monitor

def main():
    """
    Main function to start the IDS.
    """
    print("Starting IntruAlert IDS...")
    start_network_monitor()

if __name__ == '__main__':
    main()
