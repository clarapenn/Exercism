from collections import Counter


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    score = 0
    if category == ONES:
        score = 1 * dice.count(1)
    elif category == TWOS:
        score = 2 * dice.count(2)
    elif category == THREES:
        score = 3 * dice.count(3)
    elif category == FOURS:
        score = 4 * dice.count(4)
    elif category == FIVES:
        score = 5 * dice.count(5)
    elif category == SIXES:
        score = 6 * dice.count(6)
    elif category == FULL_HOUSE:
        counted = Counter(dice)
        if sorted(counted.values()) == [2, 3]:
            score = sum(dice)
    elif category == FOUR_OF_A_KIND:
        counted = Counter(dice)
        for die_face, count in counted.items():
            if count == 4:
                score = count * die_face
            if count == 5:
                score = (count - 1) * die_face
                break
    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            score = 30
    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            score = 30
    elif category == CHOICE:
        score = sum(dice)
    elif category == YACHT:
        counted = Counter(dice)
        for die_face, count in counted.items():
            if count == 5:
                score = 50
                break

    return score
