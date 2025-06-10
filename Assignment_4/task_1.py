# Read a file and handle errors 
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_content = read_file('sample.txt')
if file_content:
    print("Reading file content:")
    for idx, line in enumerate(file_content, start=1):
        print(f"Line {idx}: {line.strip()}")
    