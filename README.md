# Login Anomaly Detection Script for Financial Platforms

## Objective
Financial platforms are frequent targets of brute-force and credential-stuffing attacks. The objective of this project is to simulate detection of repeated failed login attempts using structured web access log analysis.

## Problem Context
In AI-driven trading systems, compromised accounts can lead to financial loss, unauthorized transactions, and data exposure. Detecting abnormal authentication behavior early is a critical security control.

## Tools Used
- Python 3
- VS Code
- GitHub Copilot (used for minor syntax refinement and logic suggestions)

## Detection Logic
The script parses server logs and:
- Identifies `POST` requests to `/login`
- Filters HTTP `401 Unauthorized` responses
- Counts failed attempts per IP address
- Flags IPs exceeding a defined threshold (`THRESHOLD = 3`)
- Exports suspicious IPs to a CSV report

## Project Structure
fintech-login-anomaly-detector/
├── access.log
├── analyzer.py
├── suspicious_ips.csv
├── requirements.txt
└── README.md

## How to Run
1. Open terminal in the project folder.
2. Execute:

   ```bash
   python analyzer.py
   ```

3. Check terminal output and the generated `suspicious_ips.csv` file.

## Sample Terminal Output
```text
Analyzing login attempts...

⚠ Suspicious IPs detected:

192.168.1.10 → 5 failed login attempts
203.0.113.7 → 4 failed login attempts

Results exported to suspicious_ips.csv
```

## Generated CSV Output
```csv
IP Address,Failed Attempts
192.168.1.10,5
203.0.113.7,4
```

## Screenshots for GitHub Upload
Add these images before publishing:
- Terminal run output
- Opened `suspicious_ips.csv` file
- Folder structure in VS Code Explorer

## Security Impact
This detection approach can be integrated into:
- SIEM pipelines
- Fraud detection systems
- Rate-limiting automation
- Account lockout policies

## Future Improvements
- Real-time log monitoring
- Integration with WAF or firewall automation
- Machine-learning based anomaly scoring
- Geo-IP correlation
