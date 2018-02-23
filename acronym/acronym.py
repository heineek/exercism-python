def abbreviate(phrase):
    words = phrase.replace('-', ' ').split()

    acronym_list = []
    for word in words:
        acronym_list.append(word[0].upper())

    return ''.join(acronym_list)