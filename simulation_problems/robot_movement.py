class RobotMovement:
    starting_x = 0
    starting_y = 0

    def __init__(self, x, y):
        self.starting_x = x
        self.starting_y = y

    def move_up(self, step = 1):
        self.starting_y += step

    def move_down(self, step = 1):
        self.starting_y -= step

    def move_right(self, step = 1):
        self.starting_x += step

    def move_left(self, step = 1):
        self.starting_x -= step

    def is_returned(self):
        if self.starting_x == 0 and self.starting_y == 0:
            return True

        return False

if __name__ == "__main__":
    robot_control = RobotMovement(0,0)
    robot_control.move_up(2)
    robot_control.move_down()
    robot_control.move_right()
    robot_control.move_left()
    print(robot_control.is_returned())

