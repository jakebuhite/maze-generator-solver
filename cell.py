class Cell(object):
    visited = 1
    eastWall = True
    southWall = True

    def __init__(self, x, y) -> None:
        """
        Initializes a Cell object.

        :param x: The row in which the cell is in the maze.
        :param y: The column in which the cell is in the maze.
        """
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        """
        Forms a string representation of the cell.

        :return: returns the cell coordinates in string format
        """  
        return "(x: {}, y: {})".format(self.x, self.y)
    
    def __eq__(self, cell) -> bool: 
        """
        Checks whether this cell is equal to another cell

        :param cell: The other cell that is being compared to this cell
        :return: True if cell is equal to other cell, otherwise False
        """ 
        return self.x == cell.x and self.y == cell.y
    
    def __lt__(self, cell) -> bool:
        """
        Checks whether this cell is less than another cell

        :param cell: The other cell that is being compared to this cell
        :return: True if cell is less than other cell, otherwise False
        """ 
        return self.x < cell.x or (self.x == self.y and self.y < cell.y)
    
    def __hash__(self) -> int: 
        """
        Computes the hash value for a Cell object.

        :return: A hash value based on the string representation of the cell.
        """
        return hash(str(self))