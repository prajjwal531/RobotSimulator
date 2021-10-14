from robotSimulator.robot import robot
import unittest


class TestRobot(unittest.TestCase):

    def test_if_robot_falling(self):
        r = robot(1, 1, "SOUTH")
        self.assertEqual(r.check_if_robot_is_falling(), False)

    def test_turn_left(self):
        r = robot(1, 1, "SOUTH")
        result= r.turn_left()
        self.assertEqual(result, "EAST")

    def test_turn_right(self):
        r = robot(1, 1, "SOUTH")
        result= r.turn_right()
        self.assertEqual(result, "WEST")

    def test_move(self):
        r = robot(1, 1, "SOUTH")
        x,y= (r.move())
        self.assertEqual(x, 1)
        self.assertEqual(y, 0)


if __name__ == '__main__':
    unittest.main()