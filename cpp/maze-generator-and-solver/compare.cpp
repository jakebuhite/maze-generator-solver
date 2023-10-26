#include "cell.h"
#include <tuple>

class Compare {
public:
    bool operator()(std::tuple<int, int, Cell> a, std::tuple<int, int, Cell> b)
    {
        if (std::get<0>(b) < std::get<0>(a)) {
            return true;
        }
        else if (std::get<0>(b) == std::get<0>(a) && std::get<1>(b) < std::get<1>(a)) {
            return true;
        }
        else if (std::get<0>(b) == std::get<0>(a) && std::get<1>(b) == std::get<1>(a) && std::get<2>(b) < std::get<2>(a)) {
            return true;
        }
        return false;
    }
};