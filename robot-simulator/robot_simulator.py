NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot(object):
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.x = x
        self.y = y

    @property
    def bearing(self):
        return self.direction

    @property
    def coordinates(self):
        return self.x, self.y

    def turn_right(self):
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = NORTH
        else:
            pass

    def turn_left(self):
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = NORTH
        else:
            pass

    def advance(self):
        if self.direction == NORTH:
            self.y += 1
        elif self.direction == EAST:
            self.x += 1
        elif self.direction == SOUTH:
            self.y -= 1
        else:
            self.x -= 1

    def simulate(self, control_sequence):
        actions = [action for action in control_sequence]
        for action in actions:
            if action == 'L':
                self.turn_left()
            elif action == 'R':
                self.turn_right()
            elif action == 'A':
                self.advance()
            else:
                pass