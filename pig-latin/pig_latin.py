def translate(phrase):
    do_not_move = ['xray', 'a', 'e', 'i', 'o', 'u', 'yt']
    to_move = ['squ', 'thr', 'sch', 'qu', 'th', 'ch']
    words = phrase.split()

    for pos, word in enumerate(words):
        for begin in do_not_move:
            if word.startswith(begin):
                words[pos] = word + 'ay'
                break
        else:                               # for "for" loop, not for "if"
            for begin in to_move:
                if word.startswith(begin):
                    begin_len = len(begin)
                    words[pos] = word[begin_len:] + word[:begin_len] + 'ay'
                    break
            else:                           # for "for" loop, not for "if"
                word = word[1:] + word[0] + 'ay'
                words[pos] = word

    return ' '.join(words)