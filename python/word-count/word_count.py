# from collections import Counter
# import string


# def count_words(sentence):

#     # strip standard punctuation apart from apostrophe char
#     punctuation_without_apostrophe = string.punctuation.replace("'", "")
#     for char in punctuation_without_apostrophe:
#         sentence = sentence.replace(char, " ")

#     # special case: single quotes at start and end of whole string
#     while sentence and sentence[0] == "'" and sentence[-1] == "'":
#         sentence = sentence[1:-1]

#     split_sentence = sentence.lower().split()

#     for index, word in enumerate(split_sentence):
#         while word and word[0] == "'" and word[-1] == "'":
#             word = word[1:-1]
#         split_sentence[index] = word

#     counted_words = Counter(split_sentence)

#     return dict(counted_words)


from collections import Counter
import string


def count_words(sentence):

    # strip standard punctuation apart from apostrophe char
    punctuation_without_apostrophe = string.punctuation.replace("'", "")
    for char in punctuation_without_apostrophe:
        sentence = sentence.replace(char, " ")

    split_sentence = sentence.lower().split()

    for index, word in enumerate(split_sentence):
        print("word before", word)
        # hack off leading single quotes
        while word and word[0] == "'":
            word = word[1:]
        # hack off trailing single quotes
        while word and word[-1] == "'":
            word = word[:-1]
        print("word after", word)
        split_sentence[index] = word

    print("split_sentence", split_sentence)
    split_sentence_without_empty_string = [x for x in split_sentence if x != ""]

    counted_words = Counter(split_sentence_without_empty_string)

    return dict(counted_words)
