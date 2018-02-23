def transpose(input_lines):
    if not input_lines:
        return ''

    input_list = input_lines.split('\n')
    max_len = 0
    for line in input_list:
        if len(line) > max_len:
            max_len = len(line)

    transposed = []

    for j in range(max_len):
        column = []
        for i in range(len(input_list)):
            try:
                column.append(input_list[i][j])
            except IndexError:
                column.append(' ')
        transposed.append(''.join(column))

    transposed[-1] = transposed[-1].rstrip()

    return '\n'.join(transposed)