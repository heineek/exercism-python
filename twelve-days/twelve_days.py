def verse(day):
    orders = {1: 'first', 2:'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth',
             9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth'}

    gifts = {1: 'and a Partridge in a Pear Tree.',
             2: 'two Turtle Doves',
             3: 'three French Hens',
             4: 'four Calling Birds',
             5: 'five Gold Rings',
             6: 'six Geese-a-Laying',
             7: 'seven Swans-a-Swimming',
             8: 'eight Maids-a-Milking',
             9: 'nine Ladies Dancing',
             10: 'ten Lords-a-Leaping',
             11: 'eleven Pipers Piping',
             12: 'twelve Drummers Drumming'}

    first_term = 'On the {order} day of Christmas my true love gave to me, '.format(order=orders[day])

    if day == 1:
        second_term = 'a Partridge in a Pear Tree.'
    else:
        second_term = ', '.join([gifts[x] for x in range(day, 0, -1)])

    return first_term + second_term + '\n'


def verses(begin, end):
    result = [verse(day) for day in range(begin, end+1)]
    return '\n'.join(result) + '\n'


def sing():
    return verses(1, 12)