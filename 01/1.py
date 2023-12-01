data = open("i.txt").read()
lines = data.split("\n")

count = 0
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
                lastNuzm = c
        
    count += int(arr[0] + arr[-1])

print(count)