
with open('sample.txt', 'r') as file:
    file_data = file.readlines()
print("Reading file content:")
for index, line in enumerate(file_data, start=1):
    print(f"Line {index}: {line.strip()}")


    