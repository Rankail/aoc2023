
#include "../utils.h"

long solve(std::string data) {
    auto lines = split(data, "\n");
    std::unordered_map<std::string, int> nums = {
        {"1", 1},
        {"2", 2},
        {"3", 3},
        {"4", 4},
        {"5", 5},
        {"6", 6},
        {"7", 7},
        {"8", 8},
        {"9", 9},
        {"one", 1},
        {"two", 2},
        {"three", 3},
        {"four", 4},
        {"five", 5},
        {"six", 6},
        {"seven", 7},
        {"eight", 8},
        {"nine", 9}
    };
    long sum = 0;
    for (const auto& line : lines) {
        size_t first = line.size()+1;
        long long last = -1;
        int firstNum = 0;
        int lastNum = 0;
        for (const auto& [key, val] : nums) {
            auto firstIdx = line.find(key);
            auto lastIdx = (long long)line.rfind(key);
            if (firstIdx != std::string::npos && firstIdx < first) {
                first = firstIdx;
                firstNum = val;
            }
            if (lastIdx != std::string::npos && lastIdx > last) {
                last = lastIdx;
                lastNum = val;
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
