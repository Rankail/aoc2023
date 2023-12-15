
#include <map>

#include "../utils.h"

struct Instruction {
    std::string ins[2];
};

std::string timeToString(std::chrono::high_resolution_clock::time_point start, std::chrono::high_resolution_clock::time_point end) {
    std::chrono::duration<long long, std::ratio<1, 1000000000>> duration = start - end;
    std::string result;
    auto seconds = std::chrono::duration_cast<std::chrono::seconds, long long>(duration).count();
    result += std::to_string(seconds / 60) + " min ";
    result += std::to_string(seconds % 60) + " s ";

    duration -= std::chrono::seconds(seconds);
    auto milliseconds = std::chrono::duration_cast<std::chrono::milliseconds, long long>(duration).count();
    result += std::to_string(milliseconds) + " ms ";
    duration -= std::chrono::milliseconds(milliseconds);
    auto microseconds = std::chrono::duration_cast<std::chrono::microseconds, long long>(duration).count();
    result += std::to_string(microseconds) + " µs ";
    duration -= std::chrono::microseconds (microseconds);
    auto nanoseconds = std::chrono::duration_cast<std::chrono::nanoseconds, long long>(duration).count();
    result += std::to_string(nanoseconds) + " µs ";

    return result;
}

int main(int argc, char** argv) {
    auto startTime = std::chrono::high_resolution_clock::now();


    auto data = readFile("../08/i.txt");
    auto lines = split(data, "\n");

    auto instructions = std::vector<int>();
    for (const auto& c : lines[0]) {
        instructions.emplace_back(c == 'L' ? 0 : 1);
    }

    lines = std::vector<std::string>{lines.begin()+2, lines.end()};

    auto cur = std::vector<std::string>();
    auto m = std::unordered_map<std::string, Instruction>{};
    for (const auto& line : lines) {
        auto [fromPos, toPos] = splitOnce(line, " = ");
        auto target = splitOnce(toPos.substr(1, toPos.length()-2), ", ");
        m.emplace(fromPos, Instruction{target.first, target.second});
        if (fromPos[2] == 'A') {
            cur.emplace_back(fromPos);
        }
    }

    const auto inSize = instructions.size();
    long long i = 0;
    while (true) {
        bool foundNoneZ = false;
        for (auto& pos : cur) {
            pos = m[pos].ins[instructions[i % inSize] == 0];

            if (pos[2] != 'Z') {
                foundNoneZ = true;
            }
        }

        if (i % 10000000 == 0) {
            std::cout << i / 1000000 << std::endl;
        }

        if (!foundNoneZ) {
            break;
        }

        ++i;
    }

    auto endTime = std::chrono::high_resolution_clock::now();
    std::cout << "Finished after " << timeToString(startTime, endTime);

    std::cout << i << std::endl;

    return 0;
}
