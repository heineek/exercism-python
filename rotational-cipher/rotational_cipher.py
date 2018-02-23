def rotate(msg, key):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    if key == 0 or key == 26:
        mapped_letters = letters.copy()
    else:
        mapped_letters = letters[key:]
        mapped_letters.extend(letters[:key])

    map = dict(zip(letters, mapped_letters))

    # adding capitalized letters
    for pos, key in enumerate(letters):
        map[key.upper()] = mapped_letters[pos].upper()

    result = []

    for sym in msg:
        if sym.isalpha():
            result.append(map[sym])
        else:
            result.append(sym)

    return ''.join(result)