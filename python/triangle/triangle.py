# a + b ≥ c
# b + c ≥ a
# a + c ≥ b


def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == 0 and b == 0 and c == 0:
        return False
    if a == b and a == c and b == c:
        return True

    return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == 0 and b == 0 and c == 0:
        return False
    if a + b < c and a + b != c:
        return False
    if a + c < b and a + c != c:
        return False
    if b + c < a and b + c != a:
        return False
    if (
        (a == b and a == c)
        or (b == c and a == b)
        or (a == c and b == c)
        or (a == c and a != b)
        or (a == b and b != c)
        or (b == c and a != c)
    ):
        return True

    return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == 0 and b == 0 and c == 0:
        return False
    if a + b < c and a + b != c:
        return False
    if a + c < b and a + c != c:
        return False
    if b + c < a and b + c != a:
        return False

    if a != b and a != c and b != c:
        return True
    return False
