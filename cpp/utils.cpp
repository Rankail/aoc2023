#include "utils.h"

std::string readFile(const std::string& path) {
    std::ifstream file;
    file.open(path.c_str(), std::ios::in | std::ios::binary);
    if (!file.is_open()) {
        std::cerr << "Failed to open file '" << path
            << "' from " << std::filesystem::current_path() << std::endl;
        throw std::runtime_error("Failed to open file.");
    }

    file.seekg(0, std::ios::end);
    auto size = file.tellg();
    std::string buffer(size, ' ');
    file.seekg(0, std::ios::beg);
    file.read(buffer.data(), size);

    file.close();
    return buffer;
}

std::string trim(std::string s) {
    s.erase(s.begin(), std::find_if(s.begin(), s.end(), [](unsigned char c) {
        return !std::isspace(c);
    }));

    s.erase(std::find_if(s.rbegin(), s.rend(), [](unsigned char c) {
        return !std::isspace(c);
    }).base(), s.end());

    return s;
}

std::vector<std::string> split(const std::string& s, const std::string& delim) {
    if (trim(s).empty()) {
        return {};
    }

    size_t lastDelim = 0;
    auto curDelim = s.find(delim, lastDelim);
    std::vector<std::string> parts{};

    while (curDelim != std::string::npos) {
        std::string part = s.substr(lastDelim, curDelim - lastDelim);
        parts.emplace_back(trim(part));
        lastDelim = curDelim + delim.size();
        curDelim = s.find(delim, lastDelim);
    }

    auto lastPart = s.substr(lastDelim);
    parts.emplace_back(trim(lastPart));

    return parts;
}

std::pair<std::string, std::string> splitOnce(const std::string& s, const std::string& delim) {
    auto idx = s.find(delim);
    if (idx == std::string::npos) {
        std::cerr << '"' << s << "\" cant be split at non-existent \"" << delim << '"' << std::endl;
        throw std::runtime_error("Nothin to split at");
    }

    return {s.substr(0, idx), s.substr(idx + delim.size())};
}

std::string padLeft(const std::string& s, int len) {
    return std::string(std::max(len - s.length(), 0ull), ' ') + s;
}

std::string padRight(const std::string& s, int len) {
    return s + std::string(std::max(len - s.length(), 0ull), ' ');
}