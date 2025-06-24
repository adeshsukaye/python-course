# Write and Append Data to file
file_path = "output.txt"
write_data = input("Enter text to write to the file: ").strip()
with open(file_path,'w') as file: 
    file.write(write_data.rstrip() + "\n")
print(f"Data Sussessfully written to {file_path}.\n")

append_data = input("Enter additional text to append: ").strip()
with open(file_path, 'a') as file:
    file.write(append_data.rstrip() + "\n")
print("Data successfully appended.\n")
print(f"Final content of {file_path}:")
with open(file_path, 'r') as file:
    file_content = file.read()          
print(file_content)