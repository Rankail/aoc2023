from heapq import heappush, heappop
import time

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.perf_counter()
        ret = method(*arg, **kw)
        print("Method " + method.__name__ + " took : " + "{:2.5f}".format(time.perf_counter() - t) + " sec")
        return ret

    return wrapper_method

data = open("i.txt").read()
lines = data.split("\n")

m: list[list[int]] = list()

def parseInput(lines) -> list[list[int]]:
    m = []
    for line in lines:
        row = []
        for c in line:
            row.append(int(c))
        m.append(row)
    return m

def getAtDefault(m: list[list[int]], x: int, y: int, default: int) -> int:
    if y < 0 or y >= len(m) or x < 0 or x >= len(m[0]):
        return default
    return m[y][x]

@profiler
def dijkstra(m: list[list[int]]) -> int: # accum heat
    width = len(m[0])
    height = len(m)

    visited: set[tuple[int, int, int]] = set()
    
    h = []
    heappush(h, (0, 0, 0, 0, 10)) # heat, x, y, n, dir

    while len(h) != 0:
        heat, x, y, n, dir = heappop(h)
        if (x, y, n, dir) in visited: continue
        visited.add((x, y, n, dir))
        if (x, y) == (width-1, height-1):
            return heat

        for dx, dy, ndir in ((-1,0,0), (0,-1,1), (1,0,2), (0,1,3)):
            if ndir == dir or (ndir + 2) % 4 == dir: continue # no reverse & all for that direction already covered
            nheat = heat

            for i in range(1, 4):
                nx = x + dx * i
                ny = y + dy * i
                if not (0 <= nx < width and 0 <= ny < height): break # map bounds
                nheat = m[ny][nx] + nheat

                heappush(h, (nheat, nx,ny, i, ndir))

    return -1

m = parseInput(lines)
heat = dijkstra(m)

print(heat)