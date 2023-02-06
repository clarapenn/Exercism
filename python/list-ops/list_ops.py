def append(list1, list2):
    return list1 + list2


def concat(lists):
    concat_list = []
    for list in lists:
        concat_list += list
    return concat_list


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    return len(list)


def map(function, list):
    return [function(element) for element in list]


def foldl(function, list, initial):
    result = initial
    for element in list:
        result = function(result, element)
    return result


def foldr(function, list, initial):
    result = initial
    for element in reversed(list):
        result = function(element, result)
    return result


def reverse(list):
    return [el for el in reversed(list)]
