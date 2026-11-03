
import re
from collections import Counter
from datetime import datetime

log_file = "logs/auth.log"
report_file = "reports/security_report.txt"

failed_attempts = Counter()
successful_logins = 0

# Read authentication logs
with open(log_file, "r") as file:
    for line in file:

        if "Failed password" in line:
            match = re.search(
                r"from (\d+\.\d+\.\d+\.\d+)", line
            )

            if match:
                ip = match.group(1)
                failed_attempts[ip] += 1

        elif "Accepted password" in line:
            successful_logins += 1

total_failed = sum(failed_attempts.values())

# Generate report
report = []

report.append("===== LINUX LOG ANALYZER REPORT =====")
report.append("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
report.append("")
report.append("Successful Logins: " + str(successful_logins))
report.append("Failed Login Attempts: " + str(total_failed))
report.append("")
report.append("===== IP ANALYSIS =====")

for ip, count in failed_attempts.items():

    if count >= 5:
        severity = "HIGH"
    elif count >= 3:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    report.append(
        f"IP: {ip} | Attempts: {count} | Severity: {severity}"
    )

report.append("")
report.append("===== SUSPICIOUS ACTIVITY =====")

suspicious_found = False

for ip, count in failed_attempts.items():
    if count >= 3:
        report.append(
            f"WARNING: {ip} has {count} failed login attempts."
        )
        suspicious_found = True

if not suspicious_found:
    report.append("No suspicious activity detected.")

# Save report
with open(report_file, "w") as output:
    output.write("\n".join(report))

# Display report
print("\n".join(report))
print("\nReport saved successfully!")

