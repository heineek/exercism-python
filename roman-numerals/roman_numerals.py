def numeral(arabic):
    if 3000 < arabic <= 0:
        raise ValueError

    result = []

    def next_sym(sym):
        next_sym_dict = {'I': 'V', 'V': 'X', 'X': 'L', 'L': 'C', 'C': 'D', 'D': 'M'}
        return next_sym_dict[sym]

    def add_sym(sym, num):
        result = []
        if 1 <= num <= 3:               # III, XXX...
            for _ in range(num):
                result.append(sym)
        elif num == 4:                  # IV, XL...
            result.append(sym)
            result.append(next_sym(sym))
        elif 5 <= num < 9:              # V
            result.append(next_sym(sym))
            if num > 5:                 # VI, VII...
                for _ in range(num-5):
                    result.append(sym)
        elif num == 9:                  # IX
            result.append(sym)
            result.append(next_sym(next_sym(sym)))
        else:
            raise ValueError

        return tuple(result)

    thousands = arabic // 1000
    if thousands:
        for _ in range(thousands):
            result.append('M')
        arabic %= 1000

    hundreds = arabic // 100
    if hundreds:
        for sym in add_sym('C', hundreds):
            result.append(sym)
        arabic %= 100

    tens = arabic // 10
    if tens:
        for sym in add_sym('X', tens):
            result.append(sym)
        arabic %= 10

    if arabic:
        for sym in add_sym('I', arabic):
            result.append(sym)

    return ''.join(result)