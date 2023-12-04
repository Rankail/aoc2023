
#include "../utils.h"

int main(int argc, char** argv) {
    auto data = readFile("../04/i.txt");
    auto lines = split(data, "\n");

    long sum = 0;

    auto copies = std::vector<int>(lines.size(), 1);

    for (int y = 0; y < lines.size(); ++y) {
        const auto& [_, game] = splitOnce(lines[y], ": ");
        const auto& [wins, nums] = splitOnce(game, " | ");
        std::unordered_set<int> winSet{};
        for (const auto& w : split(wins, " ")) {
            const auto& s = trim(w);
            if (s.empty()) continue;

            winSet.emplace(std::stoi(s));
        }

        int count = 0;
        for (const auto& n : split(nums, " ")) {
            const auto& s = trim(n);
            if (n.empty()) continue;

            if (winSet.contains(std::stoi(s))) {
                ++count;
            }
        }

        if (count > 0) {
            for (int i = 0; i < count; ++i) {
                copies[y + i + 1] += copies[y];
            }
        }
        sum += copies[y];
    }

    std::cout << sum << std::endl;

    return 0;
}
