import os

path = os.path.dirname(os.path.realpath(__file__))

def getCppTemplate(day: int):
    return f"""
#include "../utils.h"

int main(int argc, char** argv) {{
    auto data = readFile("../{day:02}/i.txt");
    auto lines = split(data, "\\n");

    return 0;
}}
"""


for day in range(1, 26):
    p = f"{path}/{day:02}"
    if os.path.isdir(p): continue

    os.mkdir(p)
    open(p+"/i.txt", "x")
    open(p+"/i2.txt", "x")
    with open(p+"/p1.cpp", "x") as f:
        f.write(getCppTemplate(day))
    open(p+"/p2.cpp", "x")