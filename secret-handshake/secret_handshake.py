def handshake(number):
    try:
        if type(number) is str:
            number = int(number, 2)
        if number < 0:
            raise ValueError
    except ValueError:
        return []

    code_dict = {0b1: 'wink', 0b10: 'double blink', 0b100: 'close your eyes', 0b1000: 'jump'}

    result = [code_dict[number & key] for key in code_dict.keys() if number & key in code_dict]

    if number >= 0b10000:
        result.reverse()

    return result


def code(secret_code):

    actions_dict = {'wink': 0b1, 'double blink': 0b10, 'close your eyes': 0b100, 'jump': 0b1000}
    try:
        terms = [actions_dict[action] for action in secret_code]
    except KeyError:
        return '0'

    result = 0b10000 if terms != sorted(terms) else 0

    for action in secret_code:
        result = result + actions_dict[action]

    return str(bin(result))[2:]