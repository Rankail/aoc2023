
#include "../utils.h"

struct CopyRange {
    long long srcPos;
    long long dstPos;
    long long length;
};

int main(int argc, char** argv) {
    auto data = readFile("../05/i.txt");
    const auto& [seedString, rest] = splitOnce(data, "\r\n\r\n");
    auto sections = split(rest, "\r\n\r\n");

    auto currentState = std::vector<long long>();
    for (const auto& seed : split(splitOnce(seedString, ": ").second, " ")) {
        currentState.emplace_back(std::stoll(seed));
    }

    auto nextState = std::vector<long long>(currentState.size(), 0);

    for (const auto& section : sections) {
        nextState.clear();

        auto ranges = std::vector<CopyRange>();
        const auto& lines = split(section, "\r\n");
        for (int i = 1; i < lines.size(); ++i) {
            const auto& rangeNums = split(lines[i], " ");
            ranges.emplace_back(std::stoll(rangeNums[1]), std::stoll(rangeNums[0]), std::stoll(rangeNums[2]));
        }

        for (const auto& value : currentState) {
            bool found = false;

            for (const auto& range : ranges) {
                if (range.srcPos <= value && value < range.srcPos + range.length) {
                    nextState.emplace_back(value + range.dstPos - range.srcPos);
                    found = true;
                }
            }

            if (!found) {
                nextState.emplace_back(value);
            }
        }

        currentState = nextState;
    }

    auto minVal = std::numeric_limits<long long>::max();
    for (const auto& val : currentState) {
        minVal = std::min(minVal, val);
    }

    std::cout << minVal << std::endl;

    return 0;
}
