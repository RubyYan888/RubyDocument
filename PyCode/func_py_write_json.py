# func_py_write_json.py
import json

def func_py_write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# 示例用法
data = {"name": "Alice", "age": 30, "city": "New York"}
func_py_write_json(data, "data.json")
