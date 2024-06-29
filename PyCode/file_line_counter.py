# file_line_counter.py
def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    try:
        line_count = count_lines(filename)
        print(f"The file {filename} has {line_count} lines.")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
