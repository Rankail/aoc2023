import subprocess
import webbrowser
import os

path = os.path.dirname(os.path.realpath(__file__))

day = int(input("Day: "))
if 25 < day or 0 > day:
    print("invalid day")
    exit()
p = f"{path}/{day:02}"
if not os.path.isdir(p):
    os.mkdir(p)
    open(p+"/i.txt", "x")
    open(p+"/i2.txt", "x")
    with open(p+"/1.py", "x") as f:
        f.write("data = open(\"i.txt\").read()\nlines = data.split(\"\\n\")\n\n")
    open(p+"/2.py", "x")

webbrowser.open("https://adventofcode.com/")
subprocess.Popen(["code", path], shell=True)
quit()