"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    prefixed_word = "un" + word
    return prefixed_word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix
    followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = vocab_words.pop(0)
    prefixed_words = []
    for item in vocab_words:
        prefixed_words.append(prefix + item)
    prefixed_words.insert(0, prefix)
    return " :: ".join(prefixed_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    pared_text = word.removesuffix("ness")
    if pared_text[-1] == "i":
        text_as_list = list(pared_text)
        text_as_list[-1] = "y"
        return "".join(text_as_list)
    return pared_text


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """

    split_sentence = sentence.split()
    word_to_verb = split_sentence[index]
    if list(word_to_verb)[-1] == ".":
        word_without_fullstop = list(word_to_verb)[:-1]
        return "".join(word_without_fullstop) + "en"

    verbed_word = "".join(word_to_verb) + "en"
    return verbed_word
