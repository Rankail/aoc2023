data = open("i.txt").read()
lines = data.split("\n")

stars = dict()
newStars = []
count = 0

def isNum(c):
    return (c >= '0' and c <='9')

def getAt(y, x):
    if y < 0 or y >= len(lines):
        return '.'
    if x < 0 or x >= len(lines[0]):
        return '.'
    return lines[y][x]

def isSym(y, x):
    global newStars
    c = getAt(y, x)
    if (c == '*'):
        newStars.append((y, x))

    return (c != '.' and not isNum(c))

def parseNum(y, i):
    global newStars, count
    hasSym = False
    newStars = []
    if (isSym(y-1, i-1) or isSym(y, i-1) or isSym(y+1, i-1)):
        hasSym = True

    start = i
    while i < len(lines[y]) and isNum(getAt(y,i)):
        if (isSym(y-1, i) or isSym(y+1, i)):
            hasSym = True
        i += 1
    
    if (isSym(y-1, i) or isSym(y, i) or isSym(y+1, i)):
        hasSym = True

    num = lines[y][start:i]

    if (len(newStars) != 0):
        for star in newStars:
            if (star in stars):
                print(stars[star], num)
                n = int(stars[star]) * int(num)
                count += n
            else:
                stars[star] = num

    if hasSym:
        return int(num)
    else:
        return 0

for (y, line) in enumerate(lines):
    i = 0
    while (i < len(line)):
        e = line[i]
        if (isNum(e)):
            parseNum(y, i)
            while (i < len(line) and isNum(line[i])):
                i += 1
        else:
            i += 1

print(count)