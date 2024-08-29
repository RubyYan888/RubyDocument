# func_py_find_semiperfect_numbers.py
def func_py_find_semiperfect_numbers(limit):
    def sum_of_subsets(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        for i in range(1, 1 << len(divisors)):
            subset_sum = sum(divisors[j] for j in range(len(divisors)) if i & (1 << j))
            if subset_sum == num:
                return True
        return False
    
    return [n for n in range(1, limit) if sum_of_subsets(n)]

print(func_py_find_semiperfect_numbers(100))
