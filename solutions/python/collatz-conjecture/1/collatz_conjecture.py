def steps(number):
    """
    Calculates the number of steps required to reach 1 using the Collatz conjecture rules.

    Args:
        number: A positive integer.

    Returns:
        The number of steps (integer) to reach 1.

    Raises:
        ValueError: If the input number is not a positive integer.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2  # Integer division for even numbers
        else:
            number = 3 * number + 1  # For odd numbers
        count += 1
    return count
