def encode(msg):
    result = []
    rep_count = 1   # how much times the current character is repeating
    rep_char = ''   # what character is repeating

    for pos, char in enumerate(msg):
        if pos != len(msg) - 1:         # not last character
            if char == msg[pos+1]:      # next char is the same as current
                rep_char = char
                rep_count += 1
                # continue
            else:                       # next char is different
                if rep_count > 1:
                    result.append(str(rep_count))
                    rep_count = 1       # reset counter
                result.append(char)     # add char anyway
        else:                           # last character
            if rep_count > 1:
                result.append(str(rep_count))
                rep_count = 1
            result.append(char)

    return ''.join(result)


def decode(msg):
    result = []
    num_of_chars = []

    for char in msg:
        if not char.isdigit():
            if num_of_chars:                        # there was digit(s) before
                count = int(''.join(num_of_chars))
                for _ in range(count):
                    result.append(char)
                num_of_chars.clear()
            else:                                   # standalone letter
                result.append(char)
        else:                                       # current char is digit - make the numeric using num_of_chars
            num_of_chars.append(char)

    return ''.join(result)