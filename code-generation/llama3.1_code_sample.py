def check_odd_even(num):
    """
    This function checks if the given number is odd or even.

    Args:
        num (int): The input number to be checked.

    Returns:
        str: "Even" if the number is even, "Odd" otherwise.
    """
    # Check if the number is divisible by 2
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
print(check_odd_even(10))   # Output: Even
print(check_odd_even(11))   # Output: Odd