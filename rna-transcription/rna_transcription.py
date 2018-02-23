def to_rna(dna):
    dna_to_rna_map = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    # checking the DNA string
    for sym in dna:
        if sym not in dna_to_rna_map:
            return ''

    rna = []
    for nucleotide in dna:
        rna.append(dna_to_rna_map[nucleotide])

    return ''.join(rna)