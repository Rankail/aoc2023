data = open("i.txt").read()
lines = data.split("\n")

addRows = 1000000-1

galaxies = []
xOffs = [1 for _ in range(len(lines[0]))]
yOff = 0
for (y, line) in enumerate(lines):
    foundGalaxyInLine = False
    for (x, tile) in enumerate(line):
        if tile == '#':
            foundGalaxyInLine = True
            xOffs[x] = 0
            galaxies.append((x, y + yOff * addRows))


    if not foundGalaxyInLine:
        yOff += 1
    

xOffAccum = 0
for (i, xOff) in enumerate(xOffs):
    xOffAccum += xOff
    xOffs[i] = xOffAccum

for (i, galaxy) in enumerate(galaxies):
    galaxies[i] = (galaxy[0] + xOffs[galaxy[0]] * addRows, galaxy[1])

count = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        if i != j:
            count += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(count)