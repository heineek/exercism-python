def fence_pattern():
    pass


def encode(string, num_of_lines):
    lines = [list() for _ in range(num_of_lines)]
    zigzag_period = num_of_lines * 2 - 2

    for pos, char in enumerate(string):
        modulo = pos % zigzag_period
        line = modulo if modulo < num_of_lines else zigzag_period - modulo
        lines[line].append(char)

    for pos, lst in enumerate(lines):
        lines[pos] = ''.join(lst)

    return ''.join(lines)


def decode(string, num_of_lines):
    lines = [list() for _ in range(num_of_lines)]
    zigzag_period = num_of_lines * 2 - 2
    chars = list(string)
    num_of_periods = round(len(chars) / zigzag_period)

    for line_num, line in enumerate(lines):
        if line_num == 0:
            for _ in range(num_of_periods + 1):
                line.append(chars.pop(0))
        elif line_num == len(lines) -1:
            for _ in range(num_of_periods):
                line.append(chars.pop(0))
        else:
            for _ in range(num_of_periods * 2):
                line.append(chars.pop(0))

    result = []

    for pos in range(len(string)):
        modulo = pos % zigzag_period
        line = modulo if modulo < num_of_lines else zigzag_period - modulo
        result.append(lines[line].pop(0))

    return ''.join(result)