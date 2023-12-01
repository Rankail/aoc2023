data = open("i.txt").read()
lines = data.split("\n")

count = 0
for (i, line) in enumerate(lines):
    arr = []
    for c in line:
        if ('0' <= c and c <= '9'):
            arr.append(c)
    count += int(arr[0] + arr[-1])

print(count)