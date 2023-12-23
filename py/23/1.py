from collections import deque
import time

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.perf_counter()
        ret = method(*arg, **kw)
        print("Method " + method.__name__ + " took : " + "{:2.5f}".format(time.perf_counter() - t) + " sec")
        return ret

    return wrapper_method

data = open("i2.txt").read()
lines = data.split("\n")

w = len(lines[0])
h = len(lines)

def getOppositeDir(dir):
    return (-dir[0], -dir[1])

def dirIsOpposite(d1, d2):
    return (d1[0] == 0 and d1[1] == -d2[1]) or (d1[1] == 0 and d1[0] == -d2[0])

def walkUntilCrossing(start: tuple[int, int], dir: tuple[int, int], crossings: set[tuple[int, int]]):
    slopes = "<^>v"
    slopeNotDir = {
        "<": (1,0),
        ">": (-1,0),
        "^": (0,1),
        "v": (0,-1)
    }

    dirs = ((-1, 0), (0,-1), (1,0), (0,1))

    directed = 0
    count = 0

    lastDir = dir

    x = start[0] + dir[0]
    y = start[1] + dir[1]
    while (x, y) not in crossings:
        moved = False
        for dx, dy in dirs:
            if dirIsOpposite(lastDir, (dx, dy)): continue

            c = lines[y+dy][x+dx]

            if c == '#': continue
            if c in slopes:
                if slopeNotDir[c] == (dx, dy):
                    directed = 2
                else:
                    directed = 1
            
            x = x + dx
            y = y + dy
            lastDir = (dx, dy)
            count += 1
            moved = True
            break

        if not moved:
            raise ValueError("Loop error")

    return start, (x,y), count+1, directed, lastDir



def dfs(start: tuple[int, int], end: tuple[int, int], crossings: set[tuple[int, int]]):
    q: deque[tuple[int, int, int, int]] = deque()
    visited: set[tuple[int, int, int, int]] = set()
    seenCrossings = set()

    _, lastCrossing, endLen, _, lastDir = walkUntilCrossing(end, (0,-1), crossings)
    visited.add((lastCrossing[0], lastCrossing[1], lastDir[0], lastDir[1]))
    _, firstCrossing, startLen, _, lastDir = walkUntilCrossing(start, (0,1), crossings)
    visited.add((firstCrossing[0], firstCrossing[1], lastDir[0], lastDir[1]))

    seenCrossings.add(lastCrossing)
    seenCrossings.add(firstCrossing)

    q.append((firstCrossing[0], firstCrossing[1], lastDir[0], lastDir[1]))

    dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))

    edges: list[tuple[int, int, int]] = list()

    crossIdx: dict[tuple[int, int], int] = dict()
    id = 0
    for c in crossings:
        crossIdx[c] = id
        id += 1

    while q:
        cx, cy, ldx, ldy = q.popleft()
        for dx, dy in dirs:
            if (dx == 0 and dy == -ldy) or (dy == 0 and dx == -ldx): continue
            if (cx, cy, dx, dy) in visited: continue
            if lines[cy + dy][cx + dx] != '#':
                _, foundCrossing, length, directed, lastDir = walkUntilCrossing((cx, cy), (dx, dy), crossings)

                visited.add((cx, cy, dx, dy))
                visited.add((foundCrossing[0], foundCrossing[1], lastDir[0]*-1, lastDir[1] * -1))

                if foundCrossing not in seenCrossings:
                    seenCrossings.add(foundCrossing)
                    q.append((foundCrossing[0], foundCrossing[1], lastDir[0], lastDir[1]))

                if directed < 2:
                    edges.append((crossIdx[(cx, cy)], crossIdx[foundCrossing], length))
                if directed != 1:
                    edges.append((crossIdx[foundCrossing], crossIdx[(cx, cy)], length))

    return endLen+startLen, edges, crossIdx[firstCrossing], crossIdx[lastCrossing]

def findCrossings():
    crossings = []

    dirs = ((-1, 0), (0,-1), (1,0), (0,1))
    for y in range(1,h-1):
        for x in range(1,w-1):
            if lines[y][x] == '#': continue
            count = 0
            for dx, dy in dirs:
                if lines[y+dy][x+dx] != '#':
                    count += 1
            if count >= 3:
                crossings.append((x, y))

    return set(crossings)
            
def edgesToFile(edges: list[tuple[int, int, int]]):
    with open("graph.txt", "w") as f:
        for edge in edges:
            f.write(f"{edge[0]} {edge[1]}\n")

def edgesToAdjacencyList(edges: list[tuple[int, int,int]]) -> dict[int, list[tuple[int, int]]]:
    d: dict[int, list[tuple[int, int]]] = dict()
    for edge in edges:
        if edge[0] not in d:
            d[edge[0]] = []
        d[edge[0]].append((edge[1], edge[2]))

    return d

def topologicalSortUtil(adjList, v, visited, stack):
    visited[v] = True
    if v in adjList:
        for edge in adjList[v]:
            if not visited[edge[0]]:
                topologicalSortUtil(adjList, edge[0], visited, stack)

    stack.append(v)

def longestPath(adjList, start, num: int):
    stack = []
    dist = [-1] * num

    visited: list[bool] = [False] * num
    stack = []

    for i in range(num):
        if not visited[i]:
            topologicalSortUtil(adjList, i, visited, stack)

    dist[start] = 0

    while stack:
        u = stack.pop()
        if dist[u] != -1:
            if u in adjList:
                for edge in adjList[u]:
                    dist[edge[0]] = max(dist[edge[0]], dist[u]+ edge[1])

    return dist

@profiler
def solve():
    start = (lines[0].find('.'), 0)
    end = (lines[-1].find('.'), h-1)
    
    crossings = findCrossings()

    length, edges, firstNode, lastNode = dfs(start, end, crossings)
    maxNode = 0
    for edge in edges:
        maxNode = max(maxNode, edge[0])
        maxNode = max(maxNode, edge[1])

    adjList = edgesToAdjacencyList(edges)

    edgesToFile(edges)

    distances = longestPath(adjList, firstNode, maxNode+1)
    return distances[lastNode] + length

print(solve())