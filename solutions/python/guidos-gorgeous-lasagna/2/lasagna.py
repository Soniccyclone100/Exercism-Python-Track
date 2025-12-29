# Functions used in preparing Guido's gorgeous lasagna.

# Learn about Guido, the creator of the Python language:
# https://en.wikipedia.org/wiki/Guido_van_Rossum

# This is a module docstring, used to describe the functionality of a module and its functions and/or classes.

# TODO: define your EXPECTED_BAKE_TIME and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

# TODO: Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes).
    """
    return number_of_layers * PREPARATION_TIME

# TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - the number of minutes the lasagna has been baking.
    :return: int - total elapsed time (in minutes).
    """
    preparation = preparation_time_in_minutes(number_of_layers)
    return preparation + elapsed_bake_time

# Example usage (not typically included in the module, but for demonstration):
if __name__ == "__main__":
    print(bake_time_remaining(30))  # Should return 10
    print(preparation_time_in_minutes(3))  # Should return 6
    print(elapsed_time_in_minutes(3, 20))  # Should return 26