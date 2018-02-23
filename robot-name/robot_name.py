import random


class Robot(object):
    def __init__(self):
        random.seed()
        self._name = Robot.namegen()

    @staticmethod
    def namegen():
        name = ''
        for _ in range(2):
            name = name + chr(random.randint(65, 90))
        for _ in range(3):
            name = name + str(random.randint(0, 9))
        return name

    @property
    def name(self):
        return self._name

    def reset(self):
        self._name = Robot.namegen()