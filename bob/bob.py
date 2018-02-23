def hey(sentence):

    snt = sentence.strip()

    is_question = False
    is_digit = False
    is_caps_lock = True
    is_letters = False

    # is this a question?
    if snt.endswith('?'):
        is_question = True

    # are there letters, digits and/or CAPS LOCK in sentence?
    for sym in snt:
        if sym.isdigit():
            is_digit = True
        if sym.islower():
            is_caps_lock = False
        if sym.isalpha():
            is_letters = True

    # checking conditions. Order is important for passing the tests.
    result = 'Whatever.'    # default value

    if is_letters:
        if is_caps_lock:
            result = 'Whoa, chill out!'
        elif is_question:
            result = 'Sure.'
    else:                               # no letters
        if is_question:
            result = 'Sure.'
        elif is_digit:
            pass
        else:
            result = 'Fine. Be that way!'

    return result