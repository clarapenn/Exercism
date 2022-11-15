CONSONANTS_1_CHAR = [
    "b",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
]
CONSONANTS_2_CHARS = ["ch", "qu", "rh", "th", "sq"]
CONSONANTS_3_CHARS = [
    "sch",
    "squ",
    "thr",
]


def translate(text):
    translation = ""

    # look for spaces in the text, if so it needs splitting and processing separately
    if " " in text:
        translated_words = []
        for word in text.split(" "):
            translated_words.append(translate(word))
        return " ".join(translated_words)

    # Otherwise, just process a single word

    translation = handle_starts_with_vowel(text)
    if translation is not None:
        return translation

    translation = handle_word_starts_with_consonant(text)
    if translation is not None:
        return translation

    translation = handle_y_rule(text)
    if translation is not None:
        return translation

    return translation


def handle_starts_with_vowel(word):
    if word.startswith(
        (
            "a",
            "e",
            "i",
            "o",
            "u",
            "xr",
            "yt",
        )
    ):
        word += "ay"
        return word
    else:
        # if not updated, just return None so we
        # can check for it in the calling function
        return None


def get_starting_consonants(word):
    # return the starting 1, 2 or 3 consonants, or None if not relevant
    first_char = word[:1]
    first_two_chars = word[:2]
    first_three_chars = word[:3]

    if first_three_chars in CONSONANTS_3_CHARS:
        return first_three_chars

    if first_two_chars in CONSONANTS_2_CHARS:
        return first_two_chars

    if first_char in CONSONANTS_1_CHAR:
        return first_char

    return None


def handle_word_starts_with_consonant(word):
    # Detect if the first few chars are consonants,
    # and grab the letters and rearrange, then add "ay"
    starting_consonants = get_starting_consonants(word)

    if starting_consonants:
        length_of_starting_consonants = len(starting_consonants)  # could be 1, 2 or 3
        word = word[
            length_of_starting_consonants:
        ]  # copy the word, without the first few chars
        word += starting_consonants  # add them to the end
        word += "ay"
        return word

    # if no match just return None, so we can
    # check for it in the calling function
    return None


def handle_y_rule(word):
    if "y" in word:
        starting_consonants = get_starting_consonants(word)
        if starting_consonants:
            # ok, is the NEXT letter y?
            length_of_starting_consonants = len(
                starting_consonants
            )  # could be 1, 2 or 3
            if word[length_of_starting_consonants + 1] == "y":
                word = word[
                    length_of_starting_consonants:
                ]  # copy the word, without the first consonants
                word += starting_consonants  # add them to the end
                word += "ay"
                return word
        elif len(word) == 2 and word[1] == "y":
            word = word[::-1]
            word += "ay"
            return word

    else:
        return None
