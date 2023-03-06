def is_valid(isbn):

    if not isbn:
        return False

    clean_isbn = isbn.replace("-", "")

    if len(clean_isbn) != 10:
        return False

    mutiplied = []

    for index, digit in enumerate(clean_isbn):
        # work out the decreasing multiplier
        multiplier = 10 - index

        # Clean up the digits
        if digit == "X":
            if index != 9:
                # X can only come as the last digit
                return False
            digit = 10
        elif not digit.isdigit():
            return False

        # populate the lookup with the total multioplier value for each digit
        mutiplied.append(int(digit) * multiplier)

    # now we sum all the multiplied values and mod by 11
    total = sum(mutiplied)

    return total % 11 == 0
