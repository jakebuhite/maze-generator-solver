# Imports
from maze import Maze
from metrics import dataCollection

def main():
    """
    Generates a maze, performs the A* algorithm to find a path through it, 
    and prints the maze with the path marked.

    :return: None
    """
    rows = int(input("Please enter the number of rows desired: "))
    cols = int(input("Please enter the number of cols desired: "))
    maze = Maze(rows, cols)
    maze.generateMaze()
    maze.solveMaze()
    maze.printMaze(True)

if __name__ == '__main__':
    main()
    #dataCollection()