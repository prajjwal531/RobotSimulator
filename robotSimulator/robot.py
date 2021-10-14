NORTH = "NORTH"
EAST = "EAST"
WEST = "WEST"
SOUTH = "SOUTH"


class robot():

    def __int__(self):
        print("hello I am checking the initial configuration")

    def __init__(self, x=0, y=0, direction="NORTH"):
        self.x = x
        self.y = y
        self.direction = direction
        self.directions = ["EAST", "SOUTH", "WEST", "NORTH"]

    def turn_right(self):
        try:
            self.direction = self.directions[self.get_index() + 1]
        except:
            self.direction = self.directions[0]
        return self.direction

    def turn_left(self):
        try:
            self.direction = self.directions[self.get_index() - 1]
        except:
            self.direction = self.directions[3]
        return self.direction

    def move(self):

        if (self.direction == NORTH):
            self.y += 1
        elif (self.direction == EAST):
            self.x += 1
        elif (self.direction == WEST):
            self.x -= 1
        elif (self.direction == SOUTH):
            self.y -= 1
        return self.x, self.y

    def check_initial_placement(self):
        x = self.x
        y = self.y

        if (x > 5 or y >5 ) or (x < 0 or y <0 ):
            print ("=== robot is not placed on right dimension ==")
            return False
        else:
            return True

    def decision_maker(self, command):
        if command == "MOVE":
            if (not self.check_if_robot_is_falling()):
                self.move()
            else:
                print("Robot is falling in this move, hence skipping and moving to next one", self.x, self.y)

        if command == "LEFT":
            self.turn_left()

        if command == "RIGHT":
            self.turn_right()

    def check_if_robot_is_falling(self):
        """
        This command is used to check if robot is falling from surface or not
        :return:
        """
        if (self.direction == NORTH):
            if (self.y + 1 > 5):
                return True
            else:
                return False
        if (self.direction == SOUTH):
            if (self.y - 1 <= -1):
                return True
            else:
                return False
        if (self.direction == EAST):
            if (self.x + 1 > 5):
                return True
            else:
                return False

        if (self.direction == WEST):
            if (self.x - 1 <= -1):
                return True
            else:
                return False

    def get_index(self):
        return self.directions.index(self.direction)

