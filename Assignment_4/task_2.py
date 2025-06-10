# Write and Append Data to file

def write_to_file(file_path, data):
    """Write data to a file, overwriting existing content."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data.rstrip() + "\n")
        print(f"Data successfully written to {file_path}.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def append_to_file(file_path, data):
    """Append data to a file."""
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(data.rstrip() + "\n")
        print("Data successfully appended.")
    except Exception as e:
        print(f"Error appending to file: {e}")

def read_file(file_path):
    """Read and return the content of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def main():
    file_path = "output.txt"
    write_data = input("Enter text to write to the file: ").strip()
    write_to_file(file_path, write_data)
    print()

    append_data = input("Enter additional text to append: ").strip()
    append_to_file(file_path, append_data)
    print()

    print("Final content of output.txt:")
    file_content = read_file(file_path)
    print(file_content)

if __name__ == "__main__":
    main()