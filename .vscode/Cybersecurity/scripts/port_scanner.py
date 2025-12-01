import socket

# Simple port scanner
target_ip = input("Enter target IP: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print(f"Scanning {target_ip} from port {start_port} to {end_port}...\n")

open_ports = []

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print(f"Port {port} is OPEN")
        open_ports.append(port)
    sock.close()

print("\nScan complete!")
import datetime

results_file = "scan_results.txt"

with open(results_file, "a") as f:
    f.write(f"\n--- Scan run at {datetime.datetime.now()} ---\n")
    for port in open_ports:
        f.write(f"Port {port} is open\n")