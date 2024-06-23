# quick_sort.py
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    unsorted_list = [3, 6, 8, 10, 1, 2, 1]
    sorted_list = quick_sort(unsorted_list)
    print(f"Unsorted List: {unsorted_list}")
    print(f"Sorted List: {sorted_list}")
