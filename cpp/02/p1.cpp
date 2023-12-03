
#include "../utils.h"

bool checkColor(std::unordered_map<std::string, int> balls, const std::string& col, int maxNum) {
    auto it = balls.find(col);
    if (it == balls.end()) return true;

    return it->second <= maxNum;
}

int main(int argc, char** argv) {
    auto data = readFile("../02/i.txt");
    auto lines = split(data, "\n");

    int sum = 0;

    for (const auto& line : lines) {
        const auto& [game, results] = splitOnce(line, ": ");
        const auto gameId = splitOnce(game, " ").second;
        bool possible = true;
        for (const auto& result : split(results, "; ")) {
            std::unordered_map<std::string, int> balls{};
            for (const auto& ball : split(result, ", ")) {
                const auto& [num, col] = splitOnce(ball, " ");
                int n;
                try {
                    n = std::stoi(num);
                } catch (const std::invalid_argument& e) {
                    std::cerr << '"' << num << "\" is not a number" << std::endl;
                }
                auto it = balls.find(col);
                if (it != balls.end()) {
                    it->second += n;
                } else {
                    balls[col] = n;
                }
            }

            if (!(checkColor(balls, "red", 12) && checkColor(balls, "green", 13) && checkColor(balls, "blue", 14))) {
                possible = false;
                break;
            }
        }

        if (possible) {
            sum += std::stoi(gameId);
        }
    }

    std::cout << "Result: " << sum << std::endl;

    return 0;
}
