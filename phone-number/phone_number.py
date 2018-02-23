import re


class Phone(object):
    def __init__(self, phone_number):
        allowed_chars = {'(', ')', '-', '.', '+', ' '}
        self._number_list = []
        try:
            # checking for area code validity
            if phone_number.startswith('('):
                if not (2 <= int(phone_number[1]) <= 9):
                    raise ValueError

            for char in phone_number:
                if not char.isdigit() and char not in allowed_chars:
                    raise ValueError
                elif char.isdigit():
                    self._number_list.append(char)
                else:
                    continue

            # remove country code if presented
            if len(self._number_list) == 11 and self._number_list[0] == '1':
                self._number_list.pop(0)

            # should be XXNXXXXXX now, where 2 <= N <= 0, 0 <= X <= 9
            if len(self._number_list) != 10 or not (2 <= int(self._number_list[3]) <= 9):
                raise ValueError

        except ValueError:
            self._number = "0" * 10
        else:
            self._number = ''.join(self._number_list)

    @property
    def number(self):
        return self._number

    def area_code(self):
        return self._number[:3]

    def pretty(self):
        return '({}) {}-{}'.format(self._number[:3], self._number[3:6], self._number[6:])