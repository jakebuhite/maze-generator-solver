#include "cell.h"

Cell::Cell() {
    this->x = -1;
    this->y = -1;
}

Cell::Cell(int x, int y) {
    this->x = x;
    this->y = y;
}

std::string Cell::toString() const {
    return "(x: " + std::to_string(x) + ", y: " + std::to_string(y) + ")";
}

bool Cell::operator==(const Cell& cell) const {
    return this->x == cell.x && this->y == cell.y;
}

bool Cell::operator!=(const Cell& cell) const {
    return this->x != cell.x || this->y != cell.y;
}

bool Cell::operator<(const Cell& cell) const {
    return this->x < cell.x || (this->x == cell.x && this->y < cell.y);
}

int Cell::getX() {
    return x;
}

int Cell::getY() {
    return y;
}

int Cell::getVisited() {
    return visited;
}

void Cell::setX(int x) {
    this->x = x;
}

void Cell::setY(int y) {
    this->y = y;
}

void Cell::setVisited(int visited) {
    this->visited = visited;
}

bool Cell::hasEastWall() {
    return eastWall;
}

bool Cell::hasSouthWall() {
    return southWall;
}

void Cell::removeEastWall() {
    eastWall = false;
}

void Cell::removeSouthWall() {
    southWall = false;
}
