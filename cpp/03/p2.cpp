
#include "../utils.h"

typedef std::vector<std::string> Matrix;

char getAt(const Matrix& m, int x, int y) {
    if (y < 0 || y >= m.size() || x < 0 || x >= m[y].size()) return '.';

    return m[y][x];
}

bool isNum(char c) {
    return ('0' <= c && c <= '9');
}

std::unordered_set<int> newStars{};

bool isStar(const Matrix& m, int x, int y) {
    char c = getAt(m, x, y);
    if (c != '*') return false;
    newStars.emplace(x + m[0].size() * y);
    return true;
}

int parseNum(const Matrix& m, std::unordered_map<int, int>& stars, int x, int y) {
    newStars.clear();

    isStar(m, x-1, y-1);
    isStar(m, x-1, y);
    isStar(m, x-1, y+1);

    int start = x;

    while (isNum(getAt(m, x, y))) {
        isStar(m, x, y-1);
        isStar(m, x, y+1);

        ++x;
    }

    isStar(m, x, y-1);
    isStar(m, x, y);
    isStar(m, x, y+1);

    int n = std::stoi(m[y].substr(start, x - start));

    int count = 0;
    for (const auto& s : newStars) {
        auto it = stars.find(s);
        if (it != stars.end()) {
            count += it->second * n;
        } else {
            stars.emplace(s, n);
        }
    }
    return count;
}

int main(int argc, char** argv) {
    auto data = readFile("../03/i.txt");
    auto lines = split(data, "\n");

    int sum = 0;

    std::unordered_map<int, int> stars{};

    for (int y = 0; y < lines.size(); ++y) {
        int i = 0;
        while (i < lines[y].size()) {
            if (isNum(lines[y][i])) {
                int n = parseNum(lines, stars, i, y);
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
