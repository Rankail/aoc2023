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

w = len(lines[0])
h = len(lines)

def dirIsOpposite(d1, d2):
    return (d1[0] == 0 and d1[1] == -d2[1]) or (d1[1] == 0 and d1[0] == -d2[0])

# move to next crossing
def walkUntilCrossing(start: tuple[int, int], dir: tuple[int, int], crossings: set[tuple[int, int]]):
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
            
            x = x + dx
            y = y + dy
            lastDir = (dx, dy)
            count += 1
            moved = True
            break

        if not moved:
            raise ValueError("Loop error")

    return (x,y), count+1, lastDir


# get edges from connections of crossings
def dfs(start: tuple[int, int], end: tuple[int, int], crossings: set[tuple[int, int]]):
    q: deque[tuple[int, int, int, int]] = deque()
    visited: set[tuple[int, int, int, int]] = set()
    seenCrossings = set()

    lastCrossing, endLen, lastDir = walkUntilCrossing(end, (0,-1), crossings)
    visited.add((lastCrossing[0], lastCrossing[1], lastDir[0], lastDir[1]))
    firstCrossing, startLen, lastDir = walkUntilCrossing(start, (0,1), crossings)
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
            if dirIsOpposite((dx, dy), (ldx, ldy)): continue
            if (cx, cy, dx, dy) in visited: continue
            if lines[cy + dy][cx + dx] != '#':
                foundCrossing, length, lastDir = walkUntilCrossing((cx, cy), (dx, dy), crossings)

                visited.add((cx, cy, dx, dy))
                visited.add((foundCrossing[0], foundCrossing[1], lastDir[0]*-1, lastDir[1] * -1))

                if foundCrossing not in seenCrossings:
                    seenCrossings.add(foundCrossing)
                    q.append((foundCrossing[0], foundCrossing[1], lastDir[0], lastDir[1]))

                edges.append((crossIdx[(cx, cy)], crossIdx[foundCrossing], length))
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

def longestPathUtil(adjList: dict[int, list[tuple[int, int]]], path: set[int], curNode: int, curWeight: int, endNode: int):
    maxWeight = 0
    maxPath = None
    for edge in adjList[curNode]:
        if edge[0] not in path:
            path.add(edge[0])
            weight, npath = longestPathUtil(adjList, path, edge[0], curWeight + edge[1], endNode)
            if weight > maxWeight:
                maxPath = npath
                maxWeight = weight
            path.remove(edge[0])

    if maxPath == None:
        if curNode == endNode:
            return curWeight, path
        else:
            return -1, None

    return maxWeight, maxPath
    

def longestPath(adjList, start, end):
    return longestPathUtil(adjList, {start}, start, 0, end)

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

    maxDist, maxPath = longestPath(adjList, firstNode, lastNode)
    return maxDist + length

print(solve())