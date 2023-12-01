data = open("i.txt").read()
lines = data.split("\n")

count = 0
arr = []
first = 10000000000
firstNum = '0'
last = -1
lastNum = '0'

def findCustomValue(s: str, p: str, v: int):
    global first, last, firstNum, lastNum
    i = s.find(p)
    while i != -1:
        if not (i == -1):
            if i < first:
                first = i
                firstNum = str(v)
            if i > last:
                last = i
                lastNum = str(v)
        i = s.find(p, i+1)


for line in lines:
    arr = []
    first = len(line)
    last = -1
    for (i, c) in enumerate(line):
        if ('0' <= c and c <= '9'):
            if i < first:
                first = i
                firstNum = c
            if i > last:
                last = i
                lastNum = c

    findCustomValue(line, "zero", 0)
    findCustomValue(line, "one", 1)
    findCustomValue(line, "two", 2)
    findCustomValue(line, "three", 3)
    findCustomValue(line, "four", 4)
    findCustomValue(line, "five", 5)
    findCustomValue(line, "six", 6)
    findCustomValue(line, "seven", 7)
    findCustomValue(line, "eight", 8)
    findCustomValue(line, "nine", 9)
        
    count += int(firstNum + lastNum)

print(count)