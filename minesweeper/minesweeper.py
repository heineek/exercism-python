import re


class BoardError(Exception):
    pass


def board(input_board):
    if not is_valid(input_board):
        raise ValueError("The board is invalid - check it!")

    board_height = len(input_board)
    board_width = len(input_board[0])

    result = input_board[:1]

    for i in range(1, board_height - 1):
        row = input_board[i]
        modified_row = []
        for j, char in enumerate(row):
            if char != ' ':
                modified_row.append(char)
            else:
                if mines_count(i, j, input_board):
                    modified_row.append(str(mines_count(i, j, input_board)))
                else:
                    modified_row.append(' ')
        result.append(''.join(modified_row))

    result.append(input_board[-1])

    return result


def is_valid(input_board):
    board_height = len(input_board)
    board_width = len(input_board[0])

    board_top_bottom = re.compile(r'^\+-+\+$')
    board_row = re.compile(r'^\|( |\*)+\|$')

    try:
        if input_board[0] != input_board[-1]:
            raise BoardError

        for line in input_board:
            if len(line) != board_width:
                raise BoardError

        if not board_top_bottom.match(input_board[0]) or not board_top_bottom.match(input_board[-1]):
            raise BoardError

        for i in range(1, board_height-1):
            if not board_row.match(input_board[i]):
                raise BoardError

    except BoardError:
        return False
    else:
        return True


def mines_count(i, j, input_board):
    mines = 0
    for neighbor in adjacent(i, j):
        nei_i, nei_j = neighbor
        if input_board[nei_i][nei_j] == '*':
            mines += 1
    return mines


def adjacent(i, j):
    left = (i, j-1)
    left_up = (i-1, j-1)
    up = (i-1, j)
    right_up = (i-1, j+1)
    right = (i, j+1)
    right_down = (i+1, j+1)
    down = (i+1, j)
    left_down = (i+1, j-1)

    return left, left_up, up, right_up, right, right_down, down, left_down