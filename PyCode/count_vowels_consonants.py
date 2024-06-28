# count_vowels_consonants.py
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    num_vowels = sum(1 for char in text if char in vowels)
    num_consonants = sum(1 for char in text if char.isalpha() and char not in vowels)
    return num_vowels, num_consonants

if __name__ == "__main__":
    text = input("Enter a text: ")
    vowels, consonants = count_vowels_consonants(text)
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")
