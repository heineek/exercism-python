alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reverse_alphabet = alphabet[::-1]

def encode(phrase):
    phrase_letters = (sym.lower() for sym in phrase if sym.isalnum())

    map = dict(zip(alphabet, reverse_alphabet))

    result = []
    space_position = 0

    for sym in phrase_letters:
        if sym.isdigit():
            result.append(sym)
            space_position += 1
        if sym.isalpha():
            result.append(map[sym])
            space_position += 1
        if space_position % 5 == 0:
            result.append(' ')

    return ''.join(result).rstrip()


def decode(phrase):
    phrase_letters = (sym.lower() for sym in phrase if sym.isalnum())

    map = dict(zip(reverse_alphabet, alphabet))

    result = []

    for sym in phrase_letters:
        if sym.isdigit():
            result.append(sym)
        if sym.isalpha():
            result.append(map[sym])

    return ''.join(result)