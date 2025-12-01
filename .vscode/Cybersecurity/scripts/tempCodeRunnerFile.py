
import datetime

results_file = "scan_results.txt"

# Define open_ports before using it; replace [] with actual discovered ports if available
open_ports = []

with open(results_file, "a") as f:
    f.write(f"\n--- Scan run at {datetime.datetime.now()} ---\n")
    for port in open_ports:
        f.write(f"Port {port} is open\n")