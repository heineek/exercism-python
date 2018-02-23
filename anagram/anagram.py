def detect_anagrams(word, candidates):
    anagrams = []
    word_list = [sym.lower() for sym in word]
    word_list.sort()

    for candidate in candidates:
        if candidate.lower() == word.lower():
            continue
        candidate_list = [sym.lower() for sym in candidate]
        candidate_list.sort()
        if candidate_list == word_list:
            anagrams.append(candidate)

    return anagrams