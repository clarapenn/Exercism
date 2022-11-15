"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow."""

    number = int(number)

    rounds_sequence = [number, (number + 1), (number + 2)]
    return rounds_sequence


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    all_rounds = rounds_1 + rounds_2

    return all_rounds


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values )
    OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    first_last_average_of_hand = (hand[0] + hand[-1]) / 2
    median_of_hand = hand[(len(hand) // 2)]
    calculated_average = card_average(hand)

    # if calculated_average in [first_last_average_of_hand, median_of_hand]:
    #     return True

    if (
        first_last_average_of_hand == calculated_average
        or median_of_hand == calculated_average
    ):
        return True

    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_indexed_values = []
    odd_indexed_values = []

    # for index in range(0, len(hand)):
    #     if index % 2 == 0:
    #         even_indexed_values.append(hand[index])

    #     if index % 2 != 0:
    #         odd_indexed_values.append(hand[index])

    for index, card in enumerate(hand):
        if index % 2 == 0:
            even_indexed_values.append(card)

        if index % 2 != 0:
            odd_indexed_values.append(card)

    if sum(even_indexed_values) / len(even_indexed_values) == sum(
        odd_indexed_values
    ) / len(odd_indexed_values):
        return True

    return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2

    return hand
