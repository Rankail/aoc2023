data = open("i.txt").read()
lines = data.split("\n")

count = 0
arr = []
first = 10000000000
firstNum = '0'
last = -1
lastNum = '0'

def addCustomValue(s: str, p: str, v: int):
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


for (i, line) in enumerate(lines):
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

    addCustomValue(line, "zero", 0)
    addCustomValue(line, "one", 1)
    addCustomValue(line, "two", 2)
    addCustomValue(line, "three", 3)
    addCustomValue(line, "four", 4)
    addCustomValue(line, "five", 5)
    addCustomValue(line, "six", 6)
    addCustomValue(line, "seven", 7)
    addCustomValue(line, "eight", 8)
    addCustomValue(line, "nine", 9)
    
    print(firstNum, lastNum)
        
    count += int(firstNum + lastNum)

print(count)