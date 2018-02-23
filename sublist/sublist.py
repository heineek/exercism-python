EQUAL = 1
UNEQUAL = 2
SUBLIST = 3
SUPERLIST = 4


def is_sublist(smaller, bigger):
    sublist_len = len(smaller)
    i = 0
    while(i <= len(bigger) - sublist_len):
        if smaller == bigger[i:i+sublist_len]:
            return True
        i += 1
    return False


def check_lists(first, second):
    if (not first and not second) or first == second:
        result = EQUAL
    elif (not first) or (len(first) < len(second) and is_sublist(first, second)):
        result = SUBLIST
    elif (not second) or (len(first) > len(second) and is_sublist(second, first)):
        result = SUPERLIST
    else:
        result = UNEQUAL

    return result