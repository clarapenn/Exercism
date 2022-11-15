def is_isogram(string):
    letters_already_seen = []

    # Throw away the characters that are allowed to repeat - don't need to check them
    string = string.replace(" ", "")
    string = string.replace("-", "")

    split_string = list(string.lower())

    for letter in split_string:
        if letter in letters_already_seen:
            # as soon as we detect even one duplicate, we can stop
            return False
        else:
            letters_already_seen.append(letter)

    return True
