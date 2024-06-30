# binary_search.py
def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = int(input("Enter number to search: "))
    result = binary_search(arr, x)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")
