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

def move() -> tuple[int]:
    # no outer loop like in part1
    for x in range(len(lines[0])):
        found = 0
        lastStart = -1
        for y in range(len(lines)):
            if m[y][x] == 1:
                if lastStart != -1:
                    for i in range(found):
                        m[lastStart+i][x] = 2

                found = 0
                lastStart = -1
            elif lastStart == -1:
                lastStart = y

            if m[y][x] == 2:
                found += 1
                m[y][x] = 0
        
        if lastStart != -1:
            for i in range(found):
                m[lastStart+i][x] = 2
    
    for y in range(len(lines)):
        found = 0
        lastStart = -1
        for x in range(len(lines[0])):
            if m[y][x] == 1:
                if lastStart != -1:
                    for i in range(found):
                        m[y][lastStart+i] = 2

                found = 0
                lastStart = -1
            elif lastStart == -1:
                lastStart = x

            if m[y][x] == 2:
                found += 1
                m[y][x] = 0
        
        if lastStart != -1:
            for i in range(found):
                m[y][lastStart+i] = 2


    for x in range(len(lines[0])):
        found = 0
        lastStart = -1
        for y in reversed(range(len(lines))):
            if m[y][x] == 1:
                if lastStart != -1:
                    for i in range(found):
                        m[lastStart-i][x] = 2

                found = 0
                lastStart = -1
            elif lastStart == -1:
                lastStart = y

            if m[y][x] == 2:
                found += 1
                m[y][x] = 0
        
        if lastStart != -1:
            for i in range(found):
                m[lastStart-i][x] = 2
    

    tx = []

    for y in range(len(lines)):
        txr = 0
        found = 0
        lastStart = -1
        for x in reversed(range(len(lines[0]))):
            if m[y][x] == 1:
                if lastStart != -1:
                    for i in range(found):
                        txr += 2**(lastStart-i)
                        m[y][lastStart-i] = 2

                found = 0
                lastStart = -1
            elif lastStart == -1:
                lastStart = x

            if m[y][x] == 2:
                found += 1
                m[y][x] = 0
        
        if lastStart != -1:
            for i in range(found):
                txr += 2**(lastStart-i)
                m[y][lastStart-i] = 2
        
        tx.append(txr)

    # hash of boardstate
    t = tuple(tx)
    return t


memo = {}
# memoizes board-state and step to skip ahead if the same state is found again
def memoize(t: tuple[int], step) -> int:
    if t in memo:
        diff = step - memo[t]
        times = (1_000_000_000 - step) // diff
        step += times * diff
    else:
        memo[t] = step

    return step+1


step = 0
while step < 1_000_000_000:
    t = move()
    step = memoize(t, step)


count = 0
for (y, row) in enumerate(m):
    for c in row:
        if c == 2:
            count += len(m) - y  

print(count)