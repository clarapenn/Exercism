"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    end_card_value = 0
    if card in ("J", "Q", "K"):
        end_card_value = 10
    elif card == "A":
        end_card_value = 1
    else:
        end_card_value = int(card)

    return end_card_value


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    val_of_card_one = value_of_card(card_one)
    val_of_card_two = value_of_card(card_two)

    if val_of_card_one > val_of_card_two:
        return card_one
    if val_of_card_two > val_of_card_one:
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if card_one == "A":
        card_one_amount = 11
    else:
        card_one_amount = value_of_card(card_one)
    if card_two == "A":
        card_two_amount = 11
    else:
        card_two_amount = value_of_card(card_two)

    total_score = card_one_amount + card_two_amount

    if total_score <= 10:
        ace = 11
    else:
        ace = 1

    return ace


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    ten_cards = ["10", "J", "Q", "K"]

    # if card_one == 'A' and card_two in TEN_CARDS:
    #     return True
    # if card_two == 'A' and card_one in TEN_CARDS:
    #     return True
    # return False

    return (card_one == "A" and card_two in ten_cards) or (
        card_two == "A" and card_one in ten_cards
    )


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    retval = higher_card(card_one, card_two)
    return isinstance(retval, tuple)  # if it's a tuple, it must be two equal cards


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    total = value_of_card(card_one) + value_of_card(card_two)
    three_totals = [9, 10, 11]
    return total in three_totals
