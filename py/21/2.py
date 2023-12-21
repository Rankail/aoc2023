from __future__ import annotations

data = open("i.txt").read()
lines = data.split("\n")

w = len(lines[0])
h = len(lines)

def inBounds(x, y):
    return 0 <= x < w and 0 <= y < h

def memo(entrys: list[tuple[int, int]]):
    pass

def bfs(visited: set[tuple[int, int]], latest: set[tuple[int, int]], step: int):
    newFound: set[tuple[int, int]] = set()

    for x, y in latest:

        for dx, dy in ((-1, 0), (0,-1), (1,0), (0,1)):
            nx = x + dx
            ny = y + dy
            if (nx, ny) in visited: continue
            if not inBounds(nx, ny): continue
            if lines[ny][nx] == "#": continue

            newFound.add((nx, ny))
            visited.add((nx, ny))

    return visited, newFound

def solveBoardFrom(sx: int, sy: int, steps: int = 10000) -> tuple[int,int]:
    start = (sx, sy)
    states: list[list] = [0, 0]
    visited = set()
    latest: set[tuple[int, int]] = set()

    visited.add(start)
    latest.add(start)
    states[1] = 1

    i = 0
    state = 0
    while i < steps:
        visited, latest = bfs(visited, latest, i)
        states[state] += len(latest)
        state = (state + 1) % 2
        i += 1
        if len(latest) == 0: break
    
    print(i, max(states[0], states[1]))

    return max(states[0], states[1])

def solve():
    tl = solveBoardFrom(0,0)
    tr = solveBoardFrom(w-1, 0)
    bl = solveBoardFrom(0, h-1)
    br = solveBoardFrom(w-1, h-1)

    l = solveBoardFrom(0, h // 2)
    t = solveBoardFrom(w // 2, 0)
    r = solveBoardFrom(w-1, h // 2)
    b = solveBoardFrom(w // 2, h-1)

    middle = solveBoardFrom(65, 65)
    # 20462341551
    # 26501365

    cardinal = 0
    while cardinal * 131 + 65 + 1 + 196 < 26501365:
        cardinal += 1
    cardinal -= 1
    cardinalRemaining = 26501365 - (cardinal * 131 + 65 + 1 + 196)
    
    diagonal1 = 0
    while diagonal1 * 131 + 65 + 65 + 1 + 1 + 261 < 26501365:
        diagonal1 += 1
    diagonal1 -= 1
    diagonalRemaining = 26501365 - (diagonal1 * 131 + 65 + 65 + 1 + 1 + 261)

    diagonal = (diagonal1 * (diagonal1+1)) // 2

    print(cardinal, diagonal1, diagonal, cardinalRemaining, diagonalRemaining)

    count = 0

    count += 4 * cardinal * tl
    count += 4 * diagonal * l
    count += middle

    count += (diagonal1+1) * solveBoardFrom(0, 0, diagonalRemaining)
    count += (diagonal1+1) * solveBoardFrom(w-1, 0, diagonalRemaining)
    count += (diagonal1+1) * solveBoardFrom(0, h-1, diagonalRemaining)
    count += (diagonal1+1) * solveBoardFrom(w-1, h-1, diagonalRemaining)
    count += solveBoardFrom(0, 0, cardinalRemaining)
    count += solveBoardFrom(w//2, 0, cardinalRemaining)
    count += solveBoardFrom(0, h//2, cardinalRemaining)
    count += solveBoardFrom(w//2, h//2, cardinalRemaining)

    return count


# 631_223_097_098_016 high
# 631_223_155_764_761 definitly high
# 631_223_127_038_157 high and i'm stupid. Hi stupid i'm dad.
# 629_723_659_496_127 high
# 629_723_552_074_302 no - close?
# 629_723_618_429_024 nope
# 629_720_570_456_311 fml thats it

print(solve())