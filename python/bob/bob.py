import string


def is_question(ask):
    return len(ask) > 0 and ask.strip()[-1] == "?"


def is_yelling(ask):
    return ask == ask.upper() and set(string.ascii_letters).intersection(ask)


def is_question_yelling(ask):
    return is_question(ask) and is_yelling(ask)


def is_nothing(ask):
    return ask.strip() == ""


def response(input):
    """Declares a series of functions that generate Bob's answers
    to a number of conversational gambits
    """
    if is_nothing(input):
        response = "Fine. Be that way!"
    elif is_question_yelling(input):
        response = "Calm down, I know what I'm doing!"
    elif is_yelling(input):
        response = "Whoa, chill out!"
    elif is_question(input):
        response = "Sure."

    else:
        response = "Whatever."
    return response
