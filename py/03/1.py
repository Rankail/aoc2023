data = open("i.txt").read()
lines = data.split("\n")

count = 0

def isNum(c):
    return (c >= '0' and c <='9')

def isSym(c):
    return (c != '.' and not isNum(c))

def parseNum(lines, i):
    global newStars, count
    hasSym = False
    newStars = []
    if (isSym(lines[0][i]) or isSym(lines[1][i]) or isSym(lines[2][i])):
        hasSym = True

    i += 1
    start = i
    while i < len(lines[1]) and isNum(lines[1][i]):
        if (isSym(lines[0][i]) or isSym(lines[2][i])):
            hasSym = True
        i += 1
    
    if (isSym(lines[0][i]) or isSym(lines[1][i]) or isSym(lines[2][i])):
        hasSym = True

    num = lines[1][start:i]

    if hasSym:
        return int(num)
    else:
        return 0

def getFilled(lines, y):
    if y == 0:
        l = ['.' * (len(lines[0])+2)]
        l.append('.' + lines[0] + '.')
        l.append('.' + lines[1] + '.')
        return l
    
    if y == len(lines) - 1:
        l = ['.'+l+'.' for l in lines[y-1:]]
        l.append('.' * (len(lines[0])+2))
        return l
    
    return ['.'+l+'.' for l in lines[y-1:y+2]]
    

for (y, line) in enumerate(lines):
    i = 0
    while (i < len(line)):
        e = line[i]
        if (isNum(e)):
            num = parseNum(getFilled(lines, y), i)
            count += num
            while (i < len(line) and isNum(line[i])):
                i += 1
        else:
            i += 1

print(count)