# Imports
from cell import Cell
from queue import PriorityQueue
from datetime import datetime
from enum import Enum
import random

class Directions(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)

class Maze(object):
    def __init__(self, rows, cols) -> None:
        """
        Initializes a Maze object

        :param rows: The number of rows in the maze.
        :param cols: The number of columns in the maze.
        :return: None
        """ 
        # Initialize maze and rows
        self.maze = [[Cell(i, j) for j in range(cols)] for i in range(rows)]
        self.rows = rows
        self.cols = cols

        # Establish start and goal cell
        self.start = Cell(0, 0)
        self.goal = Cell(self.rows-1, self.cols-1)
        self.goal.southWall = False
        self.maze[self.goal.x][self.goal.y] = self.goal
    
    def generateMaze(self) -> None:
        """
        Generates maze using randomized iterative depth-first search.
        
        :return: None
        """ 
        # Intialize stack
        stack = []

        # Select starting cell, mark it as visited, and push it to the stack
        self.maze[self.start.x][self.start.y] = self.start
        self.maze[self.start.x][self.start.y].visited = 0
        stack.append(self.maze[self.start.x][self.start.y])

        # While the stack is not empty
        while len(stack) > 0:
            current = stack.pop()
            # Choose one of the unvisited neighbors (none if no neighbors exist)
            neighbor = self.randomNeighbor(current)
            if (neighbor is not None):
                stack.append(current)
                # Remove the wall between the current cell and the chosen cell
                self.removeWall(current, neighbor)
                # Mark the chosen cell as visited and push it to the stack
                self.maze[neighbor.x][neighbor.y].visited = 0
                stack.append(neighbor)
        
    def randomNeighbor(self, cell) -> Cell | None:
        """
        Finds all valid neighbors of cell and randomly selects one.

        :param cell: The cell whose neighbors will be validated and randomly selected from.
        :return: A neighbor of cell (Cell), or None
        """ 
        # Possible neighbors a cell can have
        possibleNeighbors = [ Cell(cell.x - 1, cell.y), Cell(cell.x, cell.y + 1), Cell(cell.x + 1, cell.y), Cell(cell.x, cell.y - 1) ]

        # List of valid neighbors
        validNeighbors = []

        for neighbor in possibleNeighbors:
            if (self.validCell(neighbor.x, neighbor.y) and self.maze[neighbor.x][neighbor.y].visited): 
                validNeighbors.append(neighbor)

        # Check if no valid neighbors before attempting to randomly select
        if (not(len(validNeighbors))): return None

        rand = random.randint(0, len(validNeighbors) - 1)
        return validNeighbors[rand]
    
    def removeWall(self, current, neighbor) -> None:
        """
        Removes wall between current cell and neighbor cell.

        :param current: The cell whose wall will be removed
        :param neighbor: A neighboring cell of current
        :return: None
        """ 
        # Calculate delta x and y
        dx = current.x - neighbor.x
        dy = current.y - neighbor.y

        if (not(dx) and dy == -1):
            self.maze[current.x][current.y].eastWall = False # Remove right wall of curr
        elif (dx == -1 and not(dy)):
            self.maze[current.x][current.y].southWall = False # Remove bottom wall of curr
        elif (not(dx) and dy):
            self.maze[neighbor.x][neighbor.y].eastWall = False # Remove right wall of neighbor
        else:
            self.maze[neighbor.x][neighbor.y].southWall = False # Remove bottom wall of neighbor

    def printMaze(self, withPath = False) -> None:
        """
        Formats and writes the maze to a text file.

        :param withPath: Determines whether the path of the maze is included (default: False)
        :return: None
        """ 
        # File in which maze will output to
        isSolved = "solved" if withPath else "unsolved" 
        filename = "maze-{}x{}-{}-".format(self.rows, self.cols, isSolved) + datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt"
        outputFile = open("mazes/" + filename, "w")

        # Top of maze
        remaining = self.cols - self.start.y - 1
        result = "+" + (("---" + "+") * self.start.y) + ("   " + "+") + (("---" + "+") * remaining) + "\n"
        
        # Remaining portion of the maze
        for i in range(self.rows):
            result += "|"
            for j in range(self.cols):
                # Check if cell has been visited
                if (withPath and self.maze[i][j].visited == 2):
                    result += " P "
                elif (self.maze[i][j].visited == 1):
                    result += " X "
                else:
                    result += "   "

                # Check if eastern wall exists
                if (self.maze[i][j].eastWall):
                    result += "|"
                else:
                    result += " "
            result += "\n+"
            for j in range(self.cols):
                # Check if southern wall exists
                if (self.maze[i][j].southWall):
                    result += "---"
                else:
                    result += "   "
                result += "+"
            result += "\n"
        
        outputFile.write(result)
        outputFile.close()

    def validCell(self, x, y) -> bool:
        """
        Checks whether a cell's x and y values are within the bounds of the Maze.

        :param x: The row in which the potential cell is in the maze
        :param y: The column in which the potential cell is in the maze
        :return: True if x and y of a cell are within the bounds of the Maze, otherwise False
        """ 
        return x >= 0 and y >= 0 and x < self.rows and y < self.cols

    def solveMaze(self) -> None:
        """
        Uses A* search algorithm to find the shortest path between the starting cell
        and the goal cell.

        :return: None
        """ 
        # Manages the cost of the cheapest path from starting cell to current cell (g(n))
        gScore = { cell: float('inf') for row in self.maze for cell in row }
        gScore[self.start] = 0

        # Manages the sum of heuristic costs with path costs (f(n) = g(n) + h(n))
        fScore = { cell: float('inf') for row in self.maze for cell in row }
        fScore[self.start] = self.mDistance(self.start, self.goal)

        # Priority queue ordered by f(n)
        frontier = PriorityQueue()
        startH = self.mDistance(self.start, self.goal)
        frontier.put((startH, startH, self.start))

        searchPath = {}
        while not frontier.empty():
            current = frontier.get()[2]
            if current == self.goal: break
            for dir in Directions:
                if self.possibleDirection(dir, current):
                    (x, y) = dir.value
                    neighbor = Cell(current.x + x, current.y + y)
                    newF = gScore[current] + 1 + self.mDistance(neighbor, self.goal)
                    if newF < fScore[neighbor]:
                        gScore[neighbor] = gScore[current] + 1
                        fScore[neighbor] = newF
                        frontier.put((newF, self.mDistance(neighbor, self.goal), neighbor))
                        searchPath[neighbor] = current
        # Starting with the goal cell, iterate through the shortest path
        cell = self.goal
        while cell != self.start:
            self.maze[cell.x][cell.y].visited = 2
            cell = searchPath[cell]
        self.maze[self.start.x][self.start.y].visited = 2

    def mDistance(self, a, b) -> int:
        """
        Calculates the heuristic cost of a cell using Manhattan Distance

        :param a: Current cell
        :param b: Succeeding cell
        :return: The heuristic cost of a cell (int)
        """ 
        return abs(a.x - b.x) + abs(a.y - b.y)

    def possibleDirection(self, dir, cell) -> bool:
        """
        Validates cell and dir and checks whether a wall exists between cell and the
        neighbor in the direction specified.

        :param dir: describe about parameter p1
        :param cell: The cell in which the next cell is determined with
        :return: True if the next cell in the direction specified is valid and no wall exists, otherwise False.
        """ 
        if (dir == Directions.EAST and self.validCell(cell.x, cell.y + 1)):
            # Neighbor is to the east of current
            return self.maze[cell.x][cell.y].eastWall == False
        elif (dir == Directions.SOUTH and self.validCell(cell.x + 1, cell.y)):
            # Neighbor is to the south of current
            return self.maze[cell.x][cell.y].southWall == False
        elif (dir == Directions.WEST and self.validCell(cell.x, cell.y - 1)):
            # Neighbor is to the west of current
            return self.maze[cell.x][cell.y - 1].eastWall == False
        elif (dir == Directions.NORTH and self.validCell(cell.x - 1, cell.y)):
            # Neighbor is to the north of current
            return self.maze[cell.x - 1][cell.y].southWall == False
        return False