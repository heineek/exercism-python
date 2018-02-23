def square_of_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum ** 2


def sum_of_squares(n):
    sum_of_squares = 0
    for i in range(1, n + 1):
        sum_of_squares += i ** 2
    return sum_of_squares


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)