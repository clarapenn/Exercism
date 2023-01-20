"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    # 1. Are they equal?
    if len(list_one) == len(list_two) and list_one == list_two:
        print("The lists are identical")
        return EQUAL

    # 2 if not, maybe one is a sublist?
    joined1 = ",".join([f"'{x}'" for x in list_one])
    joined2 = ",".join([f"'{x}'" for x in list_two])

    # print("joined1", joined1)
    # print("joined2", joined2)

    # if A is in B, then A is a sublist
    if joined2.find(joined1) != -1:
        return SUBLIST

    # TODO: 3 . check if a superlist and return SUPERLIST
    # if A contains B, then A is a superlist
    if joined1.find(joined2) != -1:
        return SUPERLIST

    # 4. if we get this far, we have not returned already,
    # which means the list must be unequal and not a sublist or a superlist
    print("The lists are not identical")
    return UNEQUAL