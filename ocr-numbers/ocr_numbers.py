'''

Let's numerate the elements (middle '_' has number of 2):

   0
   _
1 |_| 3
4 |_| 6

   5

'''

grid_to_code = {'top': {' _ ': True, '   ': False},

                'middle': {'|  ': (1,), ' _ ': (2,), '  |': (3,),
                           '|_ ': (1, 2), ' _|': (2, 3), '| |': (1, 3), '|_|': (1, 2, 3)},

                'bottom': {'|  ': (4,), ' _ ': (5,), '  |': (6,),
                           '|_ ': (4, 5), ' _|': (5, 6), '| |': (4, 6), '|_|': (4, 5, 6)}
                }

code_to_grid = {'top': {code: element for element, code in grid_to_code['top'].items()},
                'middle': {code: element for element, code in grid_to_code['middle'].items()},
                'bottom': {code: element for element, code in grid_to_code['bottom'].items()}}

grid_to_number = {(True, (1, 3), (4, 5, 6)): '0',
                  (False, (3,), (6,)): '1',
                  (True, (2, 3), (4, 5)): '2',
                  (True, (2, 3), (5, 6)): '3',
                  (False, (1, 2, 3), (6,)): '4',
                  (True, (1, 2), (5, 6)): '5',
                  (True, (1, 2), (4, 5, 6)): '6',
                  (True, (3,), (6,)): '7',
                  (True, (1, 2, 3), (4, 5, 6)): '8',
                  (True, (1, 2, 3), (5, 6)): '9'}

number_to_grid = {number: grid for grid, number in grid_to_number.items()}


def is_blank(string):
    for char in string:
        if char != ' ':
            return False
    return True


def number(digits):
    if len(digits) != 4:
        raise ValueError

    for string in digits:
        if len(string) != len(digits[0]):
            raise ValueError

    if not is_blank(digits[-1]):
        return '?'

    top_string, middle_string, bottom_string = (string for string in digits[:3])

    top_elms = [top_string[i:i+3] for i in range(0, len(top_string), 3)]
    middle_elms = [middle_string[i:i+3] for i in range(0, len(middle_string), 3)]
    bottom_elms = [bottom_string[i:i+3] for i in range(0, len(bottom_string), 3)]

    result = []

    for top, middle, bottom in zip(top_elms, middle_elms, bottom_elms):
        try:
            top_code = grid_to_code['top'][top]
            middle_code = grid_to_code['middle'][middle]
            bottom_code = grid_to_code['bottom'][bottom]
            result.append(grid_to_number[(top_code, middle_code, bottom_code)])
        except KeyError:
            result.append('?')
    return ''.join(result)


def grid(digits):

    top_string = []
    middle_string = []
    bottom_string = []

    for digit in digits:
        try:
            top, middle, bottom = number_to_grid[str(digit)]
            top_string.append(code_to_grid['top'][top])
            middle_string.append(code_to_grid['middle'][middle])
            bottom_string.append(code_to_grid['bottom'][bottom])
        except KeyError:
            raise ValueError

    blank_string = ' ' * 3 * len(digits)

    return [''.join(top_string), ''.join(middle_string), ''.join(bottom_string), blank_string]