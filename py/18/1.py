from collections import deque
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

def getDirOfChar(c):
    if c == 'D': return (0,1)
    if c == 'U': return (0,-1)
    if c == 'L': return (-1,0)
    if c == 'R': return (1,0)
    return None

count = 0
def parseDigger(lines: list[str], m: dict[tuple[int, int], int]):
    curPos = (0,0)
    maxx = 0
    maxy = 0
    minx = 10000000
    miny = 10000000
    m[curPos] = 1
    for line in lines:
        dirChar, length, color = line.split(" ")
        dx, dy = getDirOfChar(dirChar)
        length = int(length)
        for _ in range(1, length+1):
            curPos = (curPos[0]+dx, curPos[1]+dy)
            m[curPos] = 1
            maxx = max(maxx, curPos[0])
            maxy = max(maxy, curPos[1])
            minx = min(minx, curPos[0])
            miny = min(miny, curPos[1])
    return (minx, miny), (maxx, maxy)

def boundCheck(x, y, tl, br):
    return tl[0] <= x <= br[0] and tl[1] <= y <= br[1]

def bfs(m: dict[tuple[int, int], int], tl: tuple[int], br: tuple[int, int], start: tuple[int, int]):
    visited: set = set()
    visited.add(start)
    q: deque = deque()
    q.append(start)
    inner = True
    while q:
        x,y = q.popleft()

        for dx, dy in ((-1,0),(0,-1),(1,0),(0,1)):
            nx = x+dx
            ny = y+dy
            if (nx,ny) in visited: continue
            if (nx,ny) in m: continue
            if not boundCheck(nx, ny, tl, br):
                inner = False
                continue

            visited.add((nx,ny))
            q.append((nx,ny))

    return inner, visited

def clearInner(m: dict[tuple[int, int], int], tl: tuple[int,int], br: tuple[int,int]):
    inner = set(m.keys())
    outer = set()
    for y in range(tl[1], br[1]+1):
        for x in range(tl[0], br[0]+1):
            if (x,y) not in inner and (x,y) not in outer:
                isInner, visited = bfs(m, tl, br, (x,y))
                if isInner:
                    inner.update(visited)
                else:
                    outer.update(visited)
        
    return inner, outer

@profiler
def solve():
    m: dict[tuple[int, int], int] = dict()

    tl, br = parseDigger(lines, m)
    inner, outer = clearInner(m, tl, br)
    return len(inner)

print(solve())

#  0123456
# 0#######0
# 1#.....#1
# 2###...#2
# 3..#...#3
# 4..#...#4
# 5###.###5
# 6#...#..6
# 7##..###7
# 8.#....#8
# 9.######9
