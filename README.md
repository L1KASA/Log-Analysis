# Log Analysis for Django

## 🌟 Main Components
```text
Log-Analysis/
├── .venv/                     # Virtual environment
├── logs/                      # Sample log files for testing
│   ├── app1.log
│   └── app2.log
│   └── ...
├── tests/                     
│   ├── __init__.py
│   ├── test_handler_report.py # HandlerReport tests
│   ├── test_log_processor.py  # LogProcessor tests
│   └── test_main.py           # Main script tests
├── handler_report.py          # Report generation logic
├── log_processor.py           # Log parsing utilities
├── main.py                    # Entry point and CLI
├── report.py                  # Abstract Report class
└── requirements.txt           # Dependencies
```

## 🚀 Quick Start (Windows)
### Install dependencies
```pip install -r requirements.txt```
### Run tests
```pytest --cov=./ --cov-report=html```
### Generate report
```python main.py logs/*.log --report handlers.log``` or ```python main.py logs/*.log --report```
