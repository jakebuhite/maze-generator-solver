import unittest
from maze import Maze

class MainTest(unittest.TestCase):  
    def test_unexpected_keyerror(self):
        maze = Maze(4, 4)
        try:
            maze.solveMaze()
        except KeyError:
            self.fail("solveMaze() raised KeyError unexpectedly!")

if __name__ == '__main__':
    unittest.main()