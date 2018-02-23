class Luhn(object):
    def __init__(self, number):
        self.number = number

    def is_valid(self):

        # removing spaces
        num = self.number.replace(' ', '')

        # checking for length
        if len(num) <= 1:
            return False

        # checking for validity
        for char in num:
            if not char.isdigit():
                return False

        digits = [int(digit) for digit in num]

        every_second_from_end = digits[-2::-2]
        every_second_from_end_double = []
        for digit in every_second_from_end:
            twice = digit * 2
            if twice <= 9:
                every_second_from_end_double.append(twice)
            else:
                every_second_from_end_double.append(twice - 9)

        result_list = every_second_from_end_double.copy()
        result_list.extend(digits[-1::-2])

        return not (sum(result_list) % 10)