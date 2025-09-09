import socket
import re
from datetime import datetime

def is_valid_ip(ip):
    # Regular expression to validate IPv4 address
    pattern = re.compile(
        r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    )
    return pattern.match(ip) is not None

host = input("Enter a host to scan: ")

if is_valid_ip(host):
    print("This is a valid IP address")
else:
    print("This is not a valid IP address")
    exit()  # Exit the program if the IP address is not valid

output_file = "scan-results.txt"
with open(output_file, "w") as file:
    file.write(f"Scan started at: {datetime.now()}\n")  # This writes the starting date and time to the file.
                                                        # The datetime.now() function returns the current date and time.

def is_port_open(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a new socket
        sock.settimeout(1)  # This sets timeout to 1 second
        start_time = datetime.now()  # Record the start time of the port scan
        result = sock.connect_ex((host, port))
        end_time = datetime.now()  # Record the end time of the port scan
        sock.close()
        duration = end_time - start_time  # Calculate the duration of the port scan
        print(f"Checked port {port} in {duration.total_seconds()} seconds")
        return result == 0
    except Exception as e:
        print(f"Error checking port {port}: {e}")
        return False

try:
    start_time = datetime.now()  # This records the start time of the scan.
    with open(output_file, "a") as file:
        for port in range(1, 1026):
            print(f"Checking port {port}...")  # Log each port being checked
            if is_port_open(host, port):
                file.write(f"Port {port} is open.\n")
        file.write(f"Scan ended at: {datetime.now()}\n")
        file.write(f"Total scan time: {datetime.now() - start_time}\n")
except Exception as e:
    with open(output_file, "a") as file:
        file.write(f"An error has occurred: {e}\n")

# Print the contents of scan-results.txt to the terminal
with open(output_file, "r") as file:
    print("\nFinal scan results:")
    for line in file:
        print(line.strip())
