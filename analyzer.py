from collections import defaultdict
import csv

LOG_FILE = "access.log"
THRESHOLD = 3

failed_attempts = defaultdict(int)

print("\nAnalyzing login attempts...\n")

with open(LOG_FILE, "r") as file:
    for line in file:
        if '"POST /login"' in line and "401" in line:
            ip = line.split()[0]
            failed_attempts[ip] += 1

suspicious_ips = {
    ip: count for ip, count in failed_attempts.items()
    if count > THRESHOLD
}

if suspicious_ips:
    print("⚠ Suspicious IPs detected:\n")
    for ip, count in suspicious_ips.items():
        print(f"{ip} → {count} failed login attempts")
else:
    print("No suspicious activity detected.")

with open("suspicious_ips.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP Address", "Failed Attempts"])
    for ip, count in suspicious_ips.items():
        writer.writerow([ip, count])

print("\nResults exported to suspicious_ips.csv\n")
