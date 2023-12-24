import time

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.perf_counter()
        ret = method(*arg, **kw)
        print("Method " + method.__name__ + " took : " + "{:2.5f}".format(time.perf_counter() - t) + " sec")
        return ret

    return wrapper_method

test = False
if test:
    data = open("i2.txt").read()
    areaStart =  7
    areaEnd   = 27
else:
    data = open("i.txt").read()
    areaStart = 200000000000000
    areaEnd   = 400000000000000
lines = data.split("\n")

def parseCoord(s: str):
    s = s.split(",")
    return int(s[0]), int(s[1]), int(s[2])

def parse():
    hails = []
    for line in lines:
        pos, vel = line.split("@")
        pos = parseCoord(pos)
        vel = parseCoord(vel)
        hails.append((pos, vel))
    return hails

def getIntersectionT(l1, l2):
    x1 = l1[0][0]
    x2 = x1 + l1[1][0]
    x3 = l2[0][0]
    x4 = x3 + l2[1][0]
    y1 = l1[0][1]
    y2 = y1 + l1[1][1]
    y3 = l2[0][1]
    y4 = y3 + l2[1][1]
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if d == 0: return -1, -1
    t = ((x1-x3) * (y3-y4) - (y1-y3) * (x3-x4)) / d
    u = ((x1-x3) * (y1-y2) - (y1-y3) * (x1-x2)) / d
    return t, u

@profiler
def solve():
    hails = parse()

    count = 0
    for i in range(len(hails)):
        for j in range(i+1, len(hails)):
            if i != j:
                t, u = getIntersectionT(hails[i], hails[j])
                if t < 0 or u < 0: continue
                x = hails[i][0][0] + t * hails[i][1][0]
                y = hails[i][0][1] + t * hails[i][1][1]
                if areaStart <= x <= areaEnd and areaStart <= y <= areaEnd:
                    #print(f"intersection of {hails[i]} and {hails[j]} at {(x, y)}")
                    count += 1

    return count

print(solve())