def sum_of_multiples(limit, numbers):
    multiples = []
    for number in numbers:
        factor = 1
        multiple = number
        while multiple < limit:
            multiple = number * factor
            if multiple < limit and multiple not in multiples:    # if last iteration makes too big multiple
                multiples.append(multiple)                        # or there is the same multiple already in list
                                                                  # then we skip it
            factor += 1

    return sum(multiples)