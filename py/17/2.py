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

m:list[list[int]] = list()

def parseInput(lines) -> list[list[int]]:
    m = []
    for line in lines:
        row = []
        for c in line:
            row.append(int(c))
        m.append(row)
    return m

def getAtDefault(m, x, y, default):
    if y < 0 or y >= len(m) or x < 0 or x >= len(m[0]):
        return default
    return m[y][x]

# takes ~30s
@profiler
def dijkstra(m: list[list[int]], startPos: tuple[int, int]) -> int: # accum heat
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
            if (ndir + 2) % 4 == dir or ndir == dir: continue # no reverse & all for that direction already covered
            nheat = heat
            broken = False
            for i in range(1, 4):
                nx2 = x + dx * i
                ny2 = y + dy * i
                if not(0 <= nx2 < width and 0 <= ny2 < height):
                    broken = True
                    break
                nheat += m[ny2][nx2]

            if broken: continue

            for i in range(4, 11):
                nx = x + dx * i
                ny = y + dy * i
                if nx < 0 or nx >= width or ny < 0 or ny >= height: break # map bounds
                nheat = m[ny][nx] + nheat

                heappush(h, (nheat, nx,ny, i, ndir))

    return -1

m = parseInput(lines)
heat = dijkstra(m, (0,0))

print(heat)