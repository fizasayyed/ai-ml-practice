# First OP : with same prompt as that of llama3.1 and deepseek-r1
def is_even_or_odd(number):
    """
    Checks if a given number is even or odd.

    Args:
        number: The integer to check.

    Returns:
        "Even" if the number is even, "Odd" if the number is odd.
        Returns None if the input is not an integer.
    """
    if not isinstance(number, int):
        return None  # Handle cases where the input is not an integer

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Second OP : After removing this from the prompt > Make sure you only return the code and necessary comments.

def is_even_or_odd(number):
    """
    Determines if a given number is even or odd.

    Args:
        number: The integer to check.

    Returns:
        "Even" if the number is even, "Odd" if the number is odd.
        Returns an appropriate message if the input is not an integer.
    """

    if not isinstance(number, int):
        return "Input must be an integer."  # Handle non-integer input

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Example Usage:
num1 = 10
result1 = is_even_or_odd(num1)
print(f"The number {num1} is {result1}")  # Output: The number 10 is Even

num2 = 7
result2 = is_even_or_odd(num2)
print(f"The number {num2} is {result2}")  # Output: The number 7 is Odd

num3 = 3.14
result3 = is_even_or_odd(num3)
print(f"The number {num3} is {result3}")  # Output: The number 3.14 is Input must be an integer.

# Third OP: Generate a Django Boilerplate > File : gemma3_generated_code.MD
