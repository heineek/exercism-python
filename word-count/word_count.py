import re


def word_count(phrase):
    r = re.compile(r'[A-Za-z1-9]+')
    words = [word.lower() for word in re.findall(r, phrase)]

    words_dict = {}
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    return words_dict