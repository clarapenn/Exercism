"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time

    return time_remaining


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on the number of layers
    by mutliplying the number of layers by the preparation time per layer

    Args:
        number_of_layers (int): number of layers in the lasagna

    Returns:
        int: preparation time in minutes
    """

    prep_time = PREPARATION_TIME * number_of_layers
    return prep_time


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculates total cooking time so far

    Args:
        layers (int): number of layers in lasanga
        elapsed_bake_time (int): time baking so far in minutes

    Returns:
        int: total cooking time in minutes
    """
    prep_time = preparation_time_in_minutes(layers)

    total_time_cooking = prep_time + elapsed_bake_time
    return total_time_cooking
