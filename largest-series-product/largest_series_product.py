from series import slices


def largest_product(sequence, num_of_digits):
    if num_of_digits == 0:
        return 1
    if len(sequence) == 0:
        raise ValueError

    for sym in sequence:
        if not sym.isdigit():
            raise ValueError
    if num_of_digits < 0:
        raise ValueError

    subsequences = slices(sequence, num_of_digits)

    max_product = 0

    for subsequence in subsequences:
        current_product = 1
        for i in subsequence:
            current_product *= i
        if max_product < current_product:
            max_product = current_product

    return max_product