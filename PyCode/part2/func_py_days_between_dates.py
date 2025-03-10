# func_py_days_between_dates.py
from datetime import datetime

def func_py_days_between_dates(date1, date2, format="%Y-%m-%d"):
    d1, d2 = datetime.strptime(date1, format), datetime.strptime(date2, format)
    return abs((d2 - d1).days)

print(func_py_days_between_dates("2024-01-01", "2025-03-06"))
