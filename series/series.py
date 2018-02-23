def slices(sequence, num_of_digits):
    if num_of_digits > len(sequence) or not num_of_digits:
        raise ValueError()
    else:
        sequence_list = [int(sym) for sym in sequence]
        stop_pos = len(sequence) - num_of_digits + 1
        result = []
        for i in range(0, stop_pos):
            subsequence = sequence_list[i:i+num_of_digits]
            result.append(subsequence)
        return result