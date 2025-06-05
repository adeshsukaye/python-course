import math

# Using the math module for calculation
def calculate_math_operations(num):
    """
    Performs and prints mathematical operations (square root, natural logarithm, and sine) on a given number.
    Args:
        num (float): The number to perform operations on.
    Returns:
        None
    Prints:
        The square root, natural logarithm, and sine of the input number.
    """

    sqrt_num = math.sqrt(num)
    log_num = math.log(num)
    sin_num = math.sin(num)

    print(f"Square root: {sqrt_num}")
    print(f"Logarithm: {log_num}")
    print(f"Sine: {sin_num}")

num = float(input("Enter a number: "))
calculate_math_operations(num)