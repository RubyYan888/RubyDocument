# func_py_ip_validator.py
import re

def func_py_ip_validator(ip):
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip))

print(func_py_ip_validator("192.168.1.1"))
print(func_py_ip_validator("256.100.100.100"))
