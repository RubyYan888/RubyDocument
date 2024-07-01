# count_vowels.py
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"The number of vowels in the string is: {count_vowels(s)}")
