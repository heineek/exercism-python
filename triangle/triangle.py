class TriangleError(Exception):
    pass


class Triangle(object):
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise TriangleError
        else:
            self.a = side_a
            self.b = side_b
            self.c = side_c

    def kind(self):
        unique_lengths = {self.a, self.b, self.c}
        if len(unique_lengths) == 1:
            result = 'equilateral'
        elif len(unique_lengths) == 2:
            result = 'isosceles'
        else:
            result = 'scalene'

        return result