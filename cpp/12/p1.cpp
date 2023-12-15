
#include "../utils.h"

int tryPlace(const std::string& s, const std::vector<int>& nums, int numIdx) {
    auto num = nums[numIdx];
    int count = 0;

    for (int i = 0; i < (int)(s.size())-num+1; ++i) {
        bool broken = false;
        if (i + num < s.size() && s[i + num] == '#') {
            if (s[i] == '#') break;
            continue;
        }
        for (int j = 0; j < num; ++j) {
            if (s[i + j] == '.') {
                broken = true;
                break;
            }
        }
        if (!broken) {
            if (numIdx == nums.size() - 1) {
                auto l = s.find('#', i + num);
                if (l == -1) {
                    count += 1;
                }
            } else {
                if (i + num + 1 < s.size()) {
                    count += tryPlace(s.substr(i + num + 1), nums, numIdx + 1);
                }
            }
        }
        if (s[i] == '#') {
            break;
        }
    }
    return count;
}

int trySolve(const std::string& s, const std::vector<int>& nums) {
    return tryPlace(s, nums, 0);
}

int main(int argc, char** argv) {
    auto data = readFile("../12/i.txt");
    auto lines = split(data, "\n");

    auto sum = 0;
    for (const auto& line : lines) {
        const auto& [tiles, numsStr] = splitOnce(line, " ");
        const std::vector<std::string>& numStrs = split(numsStr, ",");
        std::vector<int> nums{};
        for (const auto& n : numStrs) {
            nums.emplace_back(std::stoi(n));
        }

        auto count = trySolve(tiles, nums);
        sum += count;
        std::cout << count << std::endl;

    }

    std::cout << sum << std::endl;
    return 0;
}
