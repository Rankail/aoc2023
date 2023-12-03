
#include "../utils.h"

long solve(std::string data) {
    auto lines = split(data, "\n");
    long sum = 0;
    for (const auto& line : lines) {
        int first = line.size()+1;
        int last = -1;
        int firstNum = 0;
        int lastNum = 0;
        for (int i = 0; i < line.size(); ++i) {
            auto c = line[i];
            if ('0' <= c && c <= '9') {
                if (i < first) {
                    first = i;
                    firstNum = c-'0';
                }
                if (i > last) {
                    last = i;
                    lastNum = c-'0';
                }
            }
        }
        auto num = firstNum * 10 + lastNum;
        sum += num;
    }

    return sum;
}

int main(int argc, char** argv) {
    auto data = readFile("../01/i2.txt");

    std::cout << solve(data);

    return 0;
}
