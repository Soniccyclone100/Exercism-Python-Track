def square(number):
    """
    Calculate the number of grains on a specific square (1 through 64).
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    # The number of grains is 2 to the power of (square number - 1)
    return 2 ** (number - 1)

def total():
    """
    Calculate the total number of grains on the entire chessboard (64 squares).
    """
    # The total sum is a geometric series sum, equal to 2^64 - 1
    return 2 ** 64 - 1

#Okay i guess i understand some of this now.