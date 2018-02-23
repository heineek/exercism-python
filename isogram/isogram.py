def is_isogram(phrase):
    # extract letters only
    phrase_letters_list = [sym.lower() for sym in phrase if sym.isalpha()]

    # convert to set for checking
    phrase_letters_set = set(phrase_letters_list)

    return len(phrase_letters_set) == len(phrase_letters_list)