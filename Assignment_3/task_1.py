# Calculate Factorial using a loop or recursion

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))
output = factorial(number)
print(f"Factorial of {number} is: {output}")