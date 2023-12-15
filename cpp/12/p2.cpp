
#include <future>
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

void runThreaded(std::promise<int>* result, int id, std::vector<std::string> lines) {
    auto sum = 0;
    for (int i = 0; i < lines.size(); ++i) {
        const auto& [tiles, numsStr] = splitOnce(lines[i], " ");
        const std::vector<std::string>& numStrs = split(numsStr, ",");
        std::vector<int> nums{};
        for (const auto& n : numStrs) {
            nums.emplace_back(std::stoi(n));
        }
        std::vector<int> nums5{};
        std::string tiles5;
        for (int j = 0; j < 5; ++j) {
            nums5.insert(nums5.end(), nums.begin(), nums.end());
            tiles5 += tiles;
        }

        auto count = trySolve(tiles5, nums5);
        sum += count;

        std::cout << id << ": \t" << i+1 << "/" << lines.size() << std::endl;
    }

    result->set_value(sum);
}

int main(int argc, char** argv) {
    auto data = readFile("../12/i.txt");
    auto lines = split(data, "\n");

    constexpr auto threadCount = 6;

    std::vector<std::promise<int>*> promises{threadCount, nullptr};
    std::vector<std::thread*> threads{threadCount, nullptr};
    for (int i = 0; i < threadCount; ++i) {
        unsigned startIdx = i * lines.size() / threadCount;
        unsigned endIdx = (i+1) * lines.size() / threadCount;
        auto lineParts = std::vector<std::string>{lines.begin() + startIdx, lines.begin() + endIdx};
        promises[i] = new std::promise<int>{};
        threads[i] = new std::thread{runThreaded, promises[i], i, lineParts};
    }

    for (int i = 0; i < threadCount; ++i) {
        threads[i]->join();
    }


    auto sum = 0;
    for (int i = 0; i < lines.size(); ++i) {
        const auto& [tiles, numsStr] = splitOnce(lines[i], " ");
        const std::vector<std::string>& numStrs = split(numsStr, ",");
        std::vector<int> nums{};
        for (const auto& n : numStrs) {
            nums.emplace_back(std::stoi(n));
        }
        std::vector<int> nums5{};
        std::string tiles5;
        for (int j = 0; j < 5; ++j) {
            nums5.insert(nums5.end(), nums.begin(), nums.end());
            tiles5 += tiles;
        }

        auto count = trySolve(tiles5, nums5);
        sum += count;

        std::cout << i+1 << "/" << lines.size() << std::endl;
    }

    std::cout << sum << std::endl;
    return 0;
}
