data = open("i.txt").read()
parts = data.split("\n\n")

def getReflection(part: str):
    lines = part.split("\n")

    used = set()

    vertical: set[int] = set()
    vertical.update(range(0, len(lines[0])-1))
    for line in lines:
        for x in range(0, len(line)-1):
            hasReflection = True
            for i in range(min(len(line) - x - 1, x+1)):
                if line[x-i] != line[x+i+1]:
                    if x in used:
                        hasReflection = False
                        break
                    else:
                        used.add(x)

            if not hasReflection and x in vertical:
                vertical.remove(x)

    vertical = vertical.intersection(used, vertical)

    used.clear()
    horizontal: set[int] = set(range(0, len(lines)-1))
    for x in range(0, len(lines[0])):
        for y in range(0, len(lines)-1):
            hasReflection = True
            for i in range(min(len(lines) - y-1, y+1)):
                if lines[y-i][x] != lines[y+i+1][x]:
                    if y in used:
                        hasReflection = False
                        break
                    else:
                        used.add(y)

            if not hasReflection and y in horizontal:
                horizontal.remove(y)

    horizontal = horizontal.intersection(used, horizontal)
    print("v", vertical, "h", horizontal)
    if len(horizontal) != 0:
        return 100 * (list(horizontal)[0]+1)
    return list(vertical)[0]+1

count = 0
for part in parts:
    count += getReflection(part)

print(count)

# 34487
