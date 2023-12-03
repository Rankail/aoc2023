#ifndef UTILS_H
#define UTILS_H

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <memory>
#include <algorithm>

typedef unsigned int uint;

std::string readFile(const std::string& path);

std::string trim(std::string s);

/*
Splits the string at the delimiter and returns a vector of trimmed strings.
*/
std::vector<std::string> split(const std::string& s, const std::string& delim);
std::pair<std::string, std::string> splitOnce(const std::string& s, const std::string& delim);

std::string padLeft(const std::string& s, int len);
std::string padRight(const std::string& s, int len);

#endif