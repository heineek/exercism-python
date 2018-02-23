def multiples(base, limit):
    '''
    Generates all multiples of base up to limit
    '''
    for multiplier in range(2, limit + 1):
        yield base * multiplier


def sieve(limit):
    primes = []
    if limit == 1:
        return primes
    else:
        primes.append(2)

    numerics = [num for num in range(3, limit+1, 2)]    # all the even numerics are composites but 2

    while len(numerics) > 0:
        current_prime = numerics[0]
        for composite in multiples(current_prime, limit):
            if composite in numerics:
                numerics.remove(composite)
        primes.append(numerics.pop(0))

    return primes