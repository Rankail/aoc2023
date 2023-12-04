
#include "../utils.h"

typedef std::vector<std::string> Matrix;

bool isNum(char c) {
    return ('0' <= c && c <= '9');
}

bool isSym(char c) {
    return !(isNum(c) || c == '.');
}

char getAt(const Matrix& m, int x, int y) {
    if (y < 0 || y >= m.size() || x < 0 || x >= m[y].size()) return '.';

    return m[y][x];
}

int parseNum(const Matrix& m, int x, int y) {
    bool hasSym = false;

    if (isSym(getAt(m, x-1, y-1)) || isSym(getAt(m, x-1, y)) || isSym(getAt(m, x-1, y+1))) {
        hasSym = true;
    }

    int start = x;

    while (isNum(getAt(m, x, y))) {
        if (isSym(getAt(m, x, y-1)) || isSym(getAt(m, x, y+1))) {
            hasSym = true;
        }

        ++x;
    }

    if (isSym(getAt(m, x, y-1)) || isSym(getAt(m, x, y)) || isSym(getAt(m, x, y+1))) {
        hasSym = true;
    }

    return hasSym ? std::stoi(m[y].substr(start, x - start)) : 0;
}

int main(int argc, char** argv) {
    auto data = readFile("../03/i.txt");
    auto lines = split(data, "\n");

    int sum = 0;

    for (int y = 0; y < lines.size(); ++y) {
        int i = 0;
        while (i < lines[y].size()) {
            if (isNum(lines[y][i])) {
                int n = parseNum(lines, i, y);
                sum += n;
                while (i < lines[y].size() && isNum(lines[y][i])) ++i;
            } else {
                ++i;
            }
        }
    }

    std::cout << sum << std::endl;

    return 0;
}
