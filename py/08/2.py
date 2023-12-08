import math

data = open("i.txt").read()
lines = data.split("\n")

m = dict()

lr = lines[0]
lines = lines[2:]

cur = []
for line in lines:
    fromPos, toPos = line.split(" = ")
    left, right = toPos[1:-1].split(", ")
    m[fromPos] = (left, right)
    if fromPos[2] == "A":
        cur.append(fromPos)

loops: list[list[int]] = []
for _ in range(len(cur)):
    loops.append([])

i = 0
count2 = 0
while True:
    foundNoneZ = False
    instruction = 0 if lr[i % len(lr)] == "L" else 1
    for (j, pos) in enumerate(cur):
        newPos = m[pos][instruction]
        cur[j] = newPos
        if newPos[2] != "Z":
            foundNoneZ = True
        else:
            loops[j].append(i+1)
            if len(loops[j]) == 1:
                count2 += 1
        
    i += 1
    if not foundNoneZ:
        break

    if count2 == len(cur):
        break

    if i % 10000 == 0:
        print(loops)

# if they are so nice to make the loops simple ...
print(loops)
n = loops[0][0]
for n2 in loops[1:]:
    n = math.lcm(n, n2[0])

print(n)