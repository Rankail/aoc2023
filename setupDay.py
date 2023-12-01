import subprocess
import webbrowser
import os

day = int(input("Day: "))
if 25 < day or 0 > day:
    print("invalid day")
    exit()
p = f"E:/dev/AdventOfCode/aoc2023/{day:02}"
if not os.path.isdir(p):
    os.mkdir(p)
    open(p+"/i.txt", "x")
    open(p+"/i2.txt", "x")
    with open(p+"/1.py", "x") as f:
        f.write("data = open(\"i.txt\").read()\nlines = data.split(\"\\n\")\n\n")
    open(p+"/2.py", "x")

webbrowser.open("https://adventofcode.com/")
subprocess.Popen(["code", "E:/dev/AdventOfCode/aoc2023"], shell=True)
quit()