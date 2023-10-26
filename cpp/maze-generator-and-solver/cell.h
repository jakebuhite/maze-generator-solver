#pragma once
#include <string>

class Cell {
    int visited = 1;
    bool eastWall = true;
    bool southWall = true;
    int x;
    int y;

public:
    Cell();
    Cell(int x, int y);
    std::string toString() const;

    // Operators
    bool operator==(const Cell& cell) const;
    bool operator!=(const Cell& cell) const;
    bool operator<(const Cell& cell) const;

    // Getters and setters
    int getX();
    int getY();
    int getVisited();
    void setX(int x);
    void setY(int y);
    void setVisited(int visited);
    bool hasEastWall();
    bool hasSouthWall();
    void removeEastWall();
    void removeSouthWall();
};
