from math import sqrt


def encode(phrase):
    if not phrase:
        return phrase

    phrase_list = [char.lower() for char in phrase if char.isalnum()]
    rows = int(sqrt(len(phrase_list)))
    last_row_len = len(phrase_list) - rows ** 2
    if last_row_len:        # not perfect square
        cols = rows + 1
    else:
        cols = rows

    list_of_rows = []
    i = 0
    while i <= rows ** 2:
        column = phrase_list[i:i+cols]
        list_of_rows.append(column)
        i += cols

    # padding the last row with empty chars
    # to avoid out of range indexing
    if last_row_len:
        empty_chars = cols - len(list_of_rows[-1])
        for _ in range(empty_chars):
            list_of_rows[-1].append('')

    list_of_cols = []
    for j in range(cols):
        column = []
        for i in range(rows):
            column.append(list_of_rows[i][j])
        list_of_cols.append(column)

    result_list = [''.join(item).strip() for item in list_of_cols]
    return ' '.join(result_list)