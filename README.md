
# Linux Log Analyzer

## About the Project
A Python-based cybersecurity project that analyses
Linux authentication logs to identify repeated failed
login attempts and potentially suspicious IP addresses.

## Features
- Reads authentication log files
- Detects failed and successful login attempts
- Extracts IP addresses using Regular Expressions
- Counts failed login attempts by IP
- Classifies activity into LOW, MEDIUM and HIGH severity
- Generates an automatic security report

## Technologies Used
- Python 3
- Linux Ubuntu
- Regular Expressions
- Git and GitHub

## Project Structure
linux-log-analyzer/
├── analyzer.py
├── logs/
│   └── auth.log
├── reports/
│   └── security_report.txt
└── README.md

## How to Run

1. Clone the repository.
2. Open the project folder.
3. Run:

python3 analyzer.py

## Testing
Tested using fictional sample authentication logs.

## Learning Outcomes
- Python file handling
- Linux fundamentals
- Log analysis
- IP address extraction
- Basic security monitoring

## Author
Akshara KN
