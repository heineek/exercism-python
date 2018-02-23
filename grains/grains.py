def on_square(square):
    if square < 1 or square > 64:
        raise ValueError

    return 2 ** (square - 1)

def total_after(square):
    if square < 1 or square > 64:
        raise ValueError

    total = 0
    for i in range(1, square + 1):
        total += on_square(i)

    return total