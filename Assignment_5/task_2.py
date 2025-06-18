# Demonstrate List Slicing
list1 = [ i for i in range(1,11)]
print(f"Original list: {list1}")
first_five_elements = list1[:5]
print(f"Extracted first file elements: {first_five_elements}")
first_five_elements.reverse()
print(f"Reversed extracted elements: {first_five_elements}")
