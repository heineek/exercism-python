from sieve import sieve


def prime_factors(num):
    primes = sieve(num)

    prime_factors_list = []

    for prime in primes:
        while num % prime == 0:
            prime_factors_list.append(prime)
            num = num // prime
        if num in primes:
            prime_factors_list.append(num)
            break
        else:
            continue

    prime_factors_list.sort()
    return prime_factors_list