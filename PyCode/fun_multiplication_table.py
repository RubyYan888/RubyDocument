# fun_multiplication_table.py
def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end=" ")
        print()

multiplication_table(10)
