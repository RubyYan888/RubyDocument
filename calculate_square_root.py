# calculate_square_root.py
def calculate_square_root(n):
    return n ** 0.5

if __name__ == "__main__":
    num = float(input("Enter a number: "))
    square_root = calculate_square_root(num)
    print(f"The square root of {num} is {square_root:.2f}")
