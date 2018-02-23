def is_pangram(phrase):
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

    phrase_reformated = phrase.replace(' ', '').lower()

    # extract letters only
    phrase_letters = [sym for sym in phrase_reformated if sym.isalpha()]

    # checking for including all of letters
    phrase_letters_set = set(phrase_letters)
    
    return phrase_letters_set == alphabet