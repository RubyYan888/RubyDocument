# date_difference.py
from datetime import datetime

def calculate_date_difference(date1, date2):
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    return abs((d2 - d1).days)

date1 = "2024-06-01"
date2 = "2024-06-15"
difference = calculate_date_difference(date1, date2)
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"Difference in days: {difference}")
