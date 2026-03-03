# Screenshots Instructions

Add these three screenshots to a `screenshots/` folder in the repository:

## 1. Terminal Output (terminal_output.png)
- Open terminal in the project directory
- Run: `python analyzer.py`
- Capture the full console output showing:
  - "Analyzing login attempts..."
  - "⚠ Suspicious IPs detected:"
  - IP addresses with failed attempt counts
  - "Results exported to suspicious_ips.csv"

## 2. CSV File Output (csv_output.png)
- Open `suspicious_ips.csv` in VS Code or Excel
- Show the table with columns:
  - IP Address | Failed Attempts
  - 192.168.1.10 | 5
  - 203.0.113.7 | 4

## 3. Folder Structure (folder_structure.png)
- Open VS Code Explorer
- Show the fintech-login-anomaly-detector folder tree with all files:
  - .gitignore
  - README.md
  - access.log
  - analyzer.py
  - requirements.txt
  - suspicious_ips.csv

## Upload Steps
1. Create a `screenshots/` folder in the repository root
2. Add the three PNG images to this folder
3. Commit and push to GitHub
4. The README.md will automatically reference them
