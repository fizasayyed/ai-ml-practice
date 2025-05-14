def check_odd_even(number):
    """
    Determine if a given integer is odd or even.

    Args:
        number (int): The integer to be checked.

    Returns:
        str: 'even' if the number is divisible by 2, otherwise 'odd'.
    """
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Get input from user
user_input = int(input("Enter an integer: "))
result = check_odd_even(user_input)

print(f"The number {user_input} is {result}.")