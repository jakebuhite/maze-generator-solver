//
//  maze-generator-and-solver.cpp
//  10/12/2023
//  Jake Buhite and Nick Abegg
//
#include <iostream>
#include "maze.h"

int main()
{
    int rows;
    int cols;

    srand((unsigned int)time(NULL));

    // Get rows and cols from user
    std::cout << "Please enter the number of rows desired: ";
    std::cin >> rows;
    std::cout << "Please enter the number of cols desired: ";
    std::cin >> cols;
    
    // Generate maze
    Maze maze = Maze(rows, cols);
    maze.generateMaze();
    maze.solveMaze();
    maze.printMaze(true);
}

void dataCollection() {
    return;
}
