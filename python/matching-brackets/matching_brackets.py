def is_paired(input_string):

    stack = []

    matching_brackets = {
        # If we get the bracket on the left, what is the
        # complementary bracked that would 'match' it, so
        # we can count it as a closed pair of brackets?
        "}": "{",
        "]": "[",
        ")": "(",
    }

    for char in input_string:

        # ignore any characters that aren't brackets
        if char not in [
            "(",
            ")",
            "{",
            "}",
            "[",
            "]",
        ]:  # same as matching_brackets.keys()
            # just move on to the next character
            continue

        # If there's nothing in the stack,
        # OR the top of the stack doesn't match
        # what you just got, add the new char to the stack
        hoped_for_complementary_bracket = matching_brackets.get(char)

        if not stack or stack[-1] != hoped_for_complementary_bracket:
            stack.append(char)
        else:
            # remove the item at the top of the stack
            stack.pop()

    # if, after going through all the string, there's nothing in the stack
    # that means all the brackets were matched
    if len(stack) == 0:
        return True

    # Otherwise, the brackets in input_string were not matched
    return False
