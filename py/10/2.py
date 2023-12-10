import math

data = open("i.txt").read()
lines = data.split("\n")

# can cross in that direction
map: list[list[list[bool]]] = []
# is part of loop
map2: list[list[bool]] = []

start: (int, int) = None
for (y, line) in enumerate(lines):
    row = []
    row2 = []
    for (x, tile) in enumerate(line):
        isTile = True
        # left top right bottom
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
            isTile = False
            row.append([False, False, False, False])
        row2.append(False)
    map.append(row)
    map2.append(row2)

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
    
    raise ValueError("Is not a loop")

# i hate a these special cases
def isCharOrS(c, c2):
    return c == c2 or c == 'S'

# traverse loop
curPos = start
oldDir = None
while True:
    map2[curPos[1]][curPos[0]] = True
    curPos, oldDir = checkNeigborExcept(curPos[0], curPos[1], oldDir)
    if curPos == start:
        break

# run left to right; keep track if you are inside the loop
count = 0
for y in range(len(map)):
    inside = False
    x = 0
    sc = None
    ec = None
    while x < len(map[0]):
        if map2[y][x]:
            sc = lines[y][x]
            # be careful here! you don't want to jump gaps!
            if (map[y][x][2]):
                while x < len(map[0]) and map[y][x][2]:
                    x += 1

                if x >= len(map[0]): break
                ec = lines[y][x]
                # another one: does not change state if it goes back down or up
                if not((isCharOrS(sc, 'L') and isCharOrS(ec, 'J')) or (isCharOrS(sc, 'F') and isCharOrS(ec, '7'))):
                    inside = not inside
            else:
                inside = not inside
            x += 1

        else:
            if inside:
                count += 1
            x += 1

# write map to file with loop only
with open("realMap.txt", "w") as f:
    newLines = []
    for y in range(len(map)):
        line = ""
        for x in range(len(map[0])):
            if not map2[y][x]:
                line += '.'
            else:
                line += lines[y][x]
        line += "\n"
        newLines.append(line)
    f.writelines(newLines)

print(count)