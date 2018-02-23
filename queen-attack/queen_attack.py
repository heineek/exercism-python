def board(white_position, black_position):
    if white_position == black_position:
        raise ValueError("Black and white positions are the same!")

    for i in white_position:
        if i < 0 or i > 7:
            raise ValueError("Invalid white position!")

    for i in black_position:
        if i < 0 or i > 7:
            raise ValueError("Invalid black position!")

    w_i, w_j = white_position
    b_i, b_j = black_position

    result = ['_' * 8 for _ in range(8)]

    w_row = [char for char in result[w_i]]
    w_row[w_j] = 'W'
    result[w_i] = ''.join(w_row)

    b_row = [char for char in result[b_i]]
    b_row[b_j] = 'B'
    result[b_i] = ''.join(b_row)

    return result


def is_same_diagonal(white_position, black_position):
    w_i, w_j = white_position
    b_i, b_j = black_position

    return (max(w_i, b_i) - min(w_i, b_i)) == (max(w_j, b_j) - min(w_j, b_j))


def can_attack(white_position, black_position):
    if white_position == black_position:
        raise ValueError("Black and white positions are the same!")

    for i in white_position:
        if i < 0 or i > 7:
            raise ValueError("Invalid white position!")

    for i in black_position:
        if i < 0 or i > 7:
            raise ValueError("Invalid black position!")

    w_i, w_j = white_position
    b_i, b_j = black_position

    return w_i == b_i or w_j == b_j or is_same_diagonal(white_position, black_position)