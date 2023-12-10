import math

data = open("i.txt").read()
lines = data.split("\n")

# can cross in that direction
map: list[list[list[bool]]] = []

start: (int, int) = None
for (y, line) in enumerate(lines):
    row = []
    for (x, tile) in enumerate(line):
        # l t r b
        if tile == '|':
            row.append([False, True, False, True])
        elif tile == '-':
            row.append([True, False, True, False])
        elif tile == 'L':
            row.append([False, True, True, False])
        elif tile == '7':
            row.append([True, False, False, True])
        elif tile == 'F':
            row.append([False, False, True, True])
        elif tile == 'J':
            row.append([True, True, False, False])
        elif tile == 'S':
            start = (x, y)
            row.append([True, True, True, True])
        else:
            row.append([False, False, False, False])
    map.append(row)

def getDirOff(dir):
    if dir == 0:
        return (-1, 0)
    if dir == 1:
        return (0, -1)
    if dir == 2:
        return (1, 0)
    if dir == 3:
        return (0, 1)
    
# find (position, direction) you can go to except backwards
def checkNeigborExcept(x, y, oldDir):
    for dir in range(4):
        if oldDir != None and dir == (oldDir + 2) % 4: continue
        dx, dy = getDirOff(dir)
        if (y + dy < 0 or y + dy >= len(map) or x + dx < 0 or x + dx >= len(map[0])): continue
        if ((map[y][x][dir] or (x, y) == start) and map[y + dy][x + dx][(dir + 2) % 4]):
            return ((x + dx, y + dy), dir)
    
    odx, ody = getDirOff(oldDir)
    print(f"No tile found at {x} {y} coming from {(x - odx, y - ody)}")
    return None, None

count = 0   
curPos = start
oldDir = None
while True:
    curPos, oldDir = checkNeigborExcept(curPos[0], curPos[1], oldDir)
    if curPos == start:
        break
    count += 1

print(math.ceil(count / 2))