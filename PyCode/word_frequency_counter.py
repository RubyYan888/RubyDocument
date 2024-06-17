def word_frequency_counter(text):
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def display_frequency(frequency):
    for word, count in frequency.items():
        print(f"{word}: {count}")

def main():
    text = input("Enter some text: ")
    frequency = word_frequency_counter(text)
    display_frequency(frequency)

if __name__ == "__main__":
    main()
