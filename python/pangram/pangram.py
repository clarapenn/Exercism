def is_pangram(sentence):
    alphabet_to_check = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    lower_sentence = sentence.lower()
    target_string = list(lower_sentence)

    for letter in alphabet_to_check:
        if letter not in target_string:
            return False

    return True
