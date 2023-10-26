#pragma once
#include <vector>
#include <stack>
#include <unordered_map>
#include <queue>
#include <iostream>
#include <ctime>
#include "cell.h"

enum class Directions { NORTH = 0, EAST = 1, SOUTH = 2, WEST = 3 };

class Compare {
public:
	bool operator()(const std::tuple<int, int, Cell>& a, const std::tuple<int, int, Cell>& b) const {
		if (std::get<0>(b) < std::get<0>(a))
			return true;
		else if (std::get<0>(b) == std::get<0>(a) && std::get<1>(b) < std::get<1>(a))
			return true;
		else if (std::get<0>(b) == std::get<0>(a) && std::get<1>(b) == std::get<1>(a) && std::get<2>(b) < std::get<2>(a))
			return true;
		return false;
	}
};

class Maze {
private:
	std::vector<std::vector<Cell>> maze;
	int rows, cols;
	Cell start, goal;

	Cell* randomNeighbor(Cell& cell);
	void removeWall(Cell& current, Cell& neighbor);
	bool validCell(int x, int y);
	int mDistance(Cell& a, Cell& b);
	bool possibleDirection(Directions dir, Cell& cell);
	std::string repeat(std::string s, int n);
public:
	Maze(int rows, int cols);
	void generateMaze();
	void solveMaze();
	void printMaze(bool withPath = false);
};