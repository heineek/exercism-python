def largest_palindrome(max_factor, min_factor=1):
    max_pal = min_factor * min_factor
    curr_factors = []
    for i in range(max_factor, min_factor-1, -1):
        for j in range(max_factor, min_factor-1, -1):
            product = i * j
            if product > max_pal and str(product) == str(product)[::-1]:
                max_pal = product
                curr_factors = [i, j]
    return max_pal, tuple(curr_factors)


def smallest_palindrome(max_factor, min_factor=1):
    for i in range(min_factor, max_factor+1):
        for j in range(min_factor, max_factor+1):
            product = i * j
            if str(product) == str(product)[::-1]:
                return product, (i, j)