# func_py_generate_balanced_parentheses.py
def func_py_generate_balanced_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right)
    
    result = []
    backtrack("", 0, 0)
    return result

print(func_py_generate_balanced_parentheses(3))
