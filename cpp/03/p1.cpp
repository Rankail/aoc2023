
#include "../utils.h"

int main(int argc, char** argv) {
    auto data = readFile("./03/i.txt");
    auto lines = split(data, "\n");

    return 0;
}
