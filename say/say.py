numeric_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
                '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten',
                '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
                '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty',
                '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty',
                '90': 'ninety'}


def say_up_to_19(numeric):
    '''
    Just say it!
    '''
    return numeric_dict[str(numeric)]


def say_20_to_99(numeric):
    '''
    Add dash between tens and ones
    '''
    tens = numeric // 10
    ones = numeric % 10
    if ones == 0:
        result = numeric_dict[str(tens * 10)]
    else:
        result = numeric_dict[str(tens * 10)] + '-' + numeric_dict[str(ones)]

    return result


def say_hundreds(hundreds, modulo):
    result = [numeric_dict[str(hundreds)], 'hundred']
    if modulo:
        result.append('and')
        if 1 <= modulo <= 19:
            result.append(say_up_to_19(modulo))
        else:
            result.append(say_20_to_99(modulo))
    return ' '.join(result)


def say_three_digits_group(group):
    '''
    say 'bla-bla-bla' millions (billions, thousands...)
    '''
    if group >= 100:
        result = say_hundreds(group // 100, group % 100)
    elif 20 <= group <= 99:
        result = say_20_to_99(group)
    else:
        result = say_up_to_19(group)

    return result


def say(numeric):
    result = []

    num = int(numeric)

    if num > 999999999999 or num < 0:
        raise AttributeError()

    if num == 0:
        result.append('zero')

    # divide numeric to groups of three digits from left to right
    
    billions = num // 1000000000
    if billions:
        modulo = num % 1000000000
        result.append(say_three_digits_group(billions))
        result.append('billion')
        num = modulo

    millions = num // 1000000
    if millions:
        modulo = num % 1000000
        result.append(say_three_digits_group(millions))
        result.append('million')
        num = modulo

    thousands = num // 1000
    if thousands:
        modulo = num % 1000
        result.append(say_three_digits_group(thousands))
        result.append('thousand')
        num = modulo

    if num:
        if num < 10 and (millions or billions or thousands):
            result.append('and')
        result.append(say_three_digits_group(num))

    return ' '.join(result)