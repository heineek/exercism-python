def distance(dna_first, dna_second):

    # checking for length equivalency
    if len(dna_first) != len(dna_second):
        raise ValueError

    dna_nucleotides = {'G', 'C', 'T', 'A'}

    # checking for validity of input data
    for sym in dna_first:
        if sym not in dna_nucleotides:
            raise ValueError

    for sym in dna_second:
        if sym not in dna_nucleotides:
            raise ValueError

    diff_count = 0

    for pos, sym in enumerate(dna_first):
        if sym != dna_second[pos]:
            diff_count += 1

    return diff_count