data = open("i.txt").read()
lines = data.split("\n")

m: list[list[int]] = []
for (y, line) in enumerate(lines):
    row = []
    for c in line:
        if c == '.':
            row.append(0)
        elif c == '#':
            row.append(1)
        elif c == 'O':
            row.append(2)
    m.append(row)

for _ in range(len(lines)):
    for y in range(1,len(lines)):
        for x in range(len(lines[0])):
            if m[y][x] == 2 and m[y-1][x] == 0:
                m[y][x] = 0
                m[y-1][x] = 2

count = 0
for (y, row) in enumerate(m):
    for c in row:
        if c == 2:
            count += len(m) - y
        

print(count)