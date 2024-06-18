def is_palindrome(s):
    return s == s[::-1]

def main():
    s = "madam"
    if is_palindrome(s):
        print(f"'{s}' is a palindrome")
    else:
        print(f"'{s}' is not a palindrome")

if __name__ == "__main__":
    main()
