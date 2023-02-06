def square(number):

    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    running_total = 0

    for i in range(number):
        if i == 0:
            # First cell always has one grain on it
            number_grains = 1
        else:
            # other cells have twice the running total
            number_grains = running_total * 2
        running_total = number_grains

    return number_grains


def total():
    # if number not in range(1, 65):
    #     raise ValueError("square must be between 1 and 64")

    total_on_board = 0

    for i in range(1, 65):

        total_for_square = square(i)
        total_on_board = total_on_board + total_for_square

    return total_on_board
