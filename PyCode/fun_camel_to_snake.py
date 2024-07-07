# fun_camel_to_snake.py
import re

def fun_camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

print(fun_camel_to_snake('CamelCaseString'))
