# set_operations.py
def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    return union, intersection

if __name__ == "__main__":
    set1 = set(map(int, input("Enter elements of set1 separated by space: ").split()))
    set2 = set(map(int, input("Enter elements of set2 separated by space: ").split()))
    union, intersection = set_operations(set1, set2)
    print(f"Union: {union}")
    print(f"Intersection: {intersection}")
