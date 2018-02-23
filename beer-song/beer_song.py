def verse(number):
    firstly = "{before} bottle{plural} of beer on the wall, {before} bottle{plural} of beer.\n"
    actions = {False: "Take one down and pass it around, ", True: "Go to the store and buy some more, "}
    left = "{after} bottle{plural} of beer on the wall.\n"

    before = str(number) if number > 0 else "no more"
    if not number:
        after = 99
    else:
        after = str(number - 1) if number > 1 else "no more"
    wall_is_empty = not bool(number)
    action = actions[wall_is_empty]
    if number == 1:
        action = action.replace('one', 'it')
    plural = {'1': ''}

    result = firstly.format(before=before, plural=plural.get(before, 's')).capitalize() + \
             action + \
             left.format(after=after, plural=plural.get(after, 's'))

    return result


def song(number1, number2=0):
    result = []
    while number1 >= number2:
        result.append(verse(number1))
        number1 -= 1

    return '\n'.join(result) + '\n'