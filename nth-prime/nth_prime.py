def nth_prime(n):
    if n == 0:
        raise ValueError
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        primes_counter = 2
        cur_num = 3
        cur_prime = 3
        while primes_counter <= n:
            for divider in range(3, cur_num):
                if cur_num % divider == 0:
                    cur_num += 2
                    break
            else:
                primes_counter += 1
                cur_prime = cur_num
                cur_num += 2

        return cur_prime