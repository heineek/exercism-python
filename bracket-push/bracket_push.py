def check_brackets(string):
    brackets = {'[', ']', '{', '}', '(', ')'}
    brackets_parity = {'[': ']', '{': '}', '(': ')'}
    brackets_in_string = [bracket for bracket in string if bracket in brackets]

    if not string:          # ""
        return True

    if len(brackets_in_string) % 2:  # number of brackets is not even
        return False

    half_len = int(len(brackets_in_string) / 2)
    most_internal_bracket = brackets_in_string[half_len - 1]
    if most_internal_bracket in brackets_parity and \
            brackets_in_string[half_len] != brackets_parity[most_internal_bracket]:     # incorrectly nested ([]{)])
        return False

    while brackets_in_string:
        current_bracket = brackets_in_string.pop(0)
        try:
            brackets_in_string.remove(brackets_parity[current_bracket])
        except (ValueError, KeyError):
            return False
    return True