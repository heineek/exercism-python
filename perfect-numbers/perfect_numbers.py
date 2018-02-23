def divisor_generator(num):
    for i in range(1, num):
        if num % i == 0:
             yield i


def is_perfect(num):
    div_sum = 0
    for divisor in divisor_generator(num):
        div_sum += divisor
    return div_sum == num