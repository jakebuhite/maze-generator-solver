#include "maze.h"

Maze::Maze(int rows, int cols) {
    this->rows = rows;
    this->cols = cols;
    for (int i = 0; i < rows; i++) {
        std::vector<Cell> row;
        for (int j = 0; j < cols; j++)
            row.push_back(Cell(i, j));
        maze.push_back(row);
    }
    start = Cell(0, 0);
    goal = Cell(rows - 1, cols - 1);
    goal.removeSouthWall();
    maze[goal.getX()][goal.getY()] = goal;
}

void Maze::generateMaze() {
    std::stack<Cell> stack;
    maze[start.getX()][start.getY()].setVisited(0);
    stack.push(maze[start.getX()][start.getY()]);

    while (!stack.empty()) {
        Cell current = stack.top();
        stack.pop();
        Cell* neighbor = randomNeighbor(current);
        if (neighbor != nullptr) {
            stack.push(current);
            removeWall(current, *neighbor);
            neighbor->setVisited(0);
            stack.push(*neighbor);
        }
    }
}

Cell* Maze::randomNeighbor(Cell& cell) {
    Cell possibleNeighbors[4] = { Cell(cell.getX() - 1, cell.getY()), Cell(cell.getX(), cell.getY() + 1), Cell(cell.getX() + 1, cell.getY()), Cell(cell.getX(), cell.getY() - 1) };
    std::vector<Cell*> validNeighbors;

    for (auto& neighbor : possibleNeighbors) {
        if (validCell(neighbor.getX(), neighbor.getY()) && maze[neighbor.getX()][neighbor.getY()].getVisited())
            validNeighbors.push_back(&maze[neighbor.getX()][neighbor.getY()]);
    }

    if (validNeighbors.empty())
        return nullptr;

    int rand = std::rand() % validNeighbors.size();
    return validNeighbors[rand];
}

void Maze::removeWall(Cell& current, Cell& neighbor) {
    int dx = current.getX() - neighbor.getX();
    int dy = current.getY() - neighbor.getY();

    if (!dx && dy == -1)
        maze[current.getX()][current.getY()].removeEastWall();
    else if (dx == -1 && !dy)
        maze[current.getX()][current.getY()].removeSouthWall();
    else if (!dx && dy)
        maze[neighbor.getX()][neighbor.getY()].removeEastWall();
    else
        maze[neighbor.getX()][neighbor.getY()].removeSouthWall();
}

std::string Maze::repeat(std::string s, int n) {
    std::string ans = "";
    for (int i = 0; i < n; i++)
        ans += s;
    return ans;
}

void Maze::printMaze(bool withPath) {
    std::string result = "+" + repeat("---+",start.getY()) + "   +" + repeat("---+", cols - start.getY() - 1) + '\n';
    for (int i = 0; i < rows; i++) {
        result += "|";
        for (int j = 0; j < cols; j++) {
            if (withPath && maze[i][j].getVisited() == 2)
                result += " P ";
            else if (maze[i][j].getVisited() == 1)
                result += " X ";
            else
                result += "   ";

            result += (maze[i][j].hasEastWall()) ? "|" : " ";
        }
        result += "\n+";
        for (int j = 0; j < cols; j++) {
            result += (maze[i][j].hasSouthWall()) ? "---" : "   ";
            result += "+";
        }
        result += '\n';
    }
    std::cout << result;
}

bool Maze::validCell(int x, int y) { return x >= 0 && y >= 0 && x < rows && y < cols; }

void Maze::solveMaze() {
    std::unordered_map<std::string, int> gScore;
    std::unordered_map<std::string, int> fScore;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            gScore[maze[i][j].toString()] = INT_MAX;
            fScore[maze[i][j].toString()] = INT_MAX;
        }
    }

    gScore[start.toString()] = 0;
    fScore[start.toString()] = mDistance(start, goal);

    std::priority_queue<std::tuple<int, int, Cell>, std::vector<std::tuple<int, int, Cell>>, Compare> frontier;
    int startH = mDistance(start, goal);
    frontier.push({ startH, startH, start });

    std::unordered_map<std::string, Cell> searchPath;
    while (!frontier.empty()) {
        Cell current = std::get<2>(frontier.top());
        frontier.pop();
        if (current == goal) break;
        for (auto dir : { Directions::NORTH, Directions::EAST, Directions::SOUTH, Directions::WEST }) {
            if (possibleDirection(dir, current)) {
                int x = 0, y = 0;
                switch (dir) {
                case Directions::NORTH:
                    x = -1;
                    break;
                case Directions::EAST:
                    y = 1;
                    break;
                case Directions::SOUTH:
                    x = 1;
                    break;
                case Directions::WEST:
                    y = -1;
                    break;
                }
                Cell neighbor(current.getX() + x, current.getY() + y);
                int newF = gScore[current.toString()] + 1 + mDistance(neighbor, goal);
                if (newF < fScore[neighbor.toString()]) {
                    gScore[neighbor.toString()] = gScore[current.toString()] + 1;
                    fScore[neighbor.toString()] = newF;
                    frontier.push({ newF, mDistance(neighbor, goal), neighbor });
                    searchPath[neighbor.toString()] = current;
                }
            }
        }
    }
    Cell cell = goal;
    while (cell != start) {
        maze[cell.getX()][cell.getY()].setVisited(2);
        cell = searchPath[cell.toString()];
    }
    maze[start.getX()][start.getY()].setVisited(2);
}

int Maze::mDistance(Cell& a, Cell& b) { return abs(a.getX() - b.getX()) + abs(a.getY() - b.getY()); }

bool Maze::possibleDirection(Directions dir, Cell& cell) {
    switch (dir) {
    case Directions::NORTH:
        if (validCell(cell.getX() - 1, cell.getY())) {
            int i = cell.getX() - 1;
            return !maze[i][cell.getY()].hasSouthWall();
        }
        break;
    case Directions::EAST:
        if (validCell(cell.getX(), cell.getY() + 1)) {
            return !maze[cell.getX()][cell.getY()].hasEastWall();
        }
        break;
    case Directions::SOUTH:
        if (validCell(cell.getX() + 1, cell.getY())) {
            return !maze[cell.getX()][cell.getY()].hasSouthWall();
        }
        break;
    case Directions::WEST:
        if (validCell(cell.getX(), cell.getY() - 1)) {
            int j = cell.getY() - 1;
            return !maze[cell.getX()][j].hasEastWall();
        }
        break;
    }
    return false;
}
