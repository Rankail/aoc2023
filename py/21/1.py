data = open("i.txt").read()
lines = data.split("\n")

def inBounds(x, y):
    return 0 <= x < len(lines[0]) and 0 <= y < len(lines)

def bfs(visited: set[tuple[int, int]], latest: set[tuple[int, int]]):
    newFound: set[tuple[int, int]] = set()

    for x, y in latest:
        for dx, dy in ((-1, 0), (0,-1), (1,0), (0,1)):
            nx = x + dx
            ny = y + dy
            if not inBounds(nx, ny): continue
            if (nx, ny) in visited: continue
            if lines[ny][nx] == "#": continue

            newFound.add((nx, ny))
            visited.add((nx, ny))

    return visited, newFound

def solve():
    start = None
    for (y, line) in enumerate(lines):
        for (x, c) in enumerate(line):
            if c == 'S':
                start = (x, y)
    if start == None:
        raise ValueError("No start found")

    states: list[list] = [0, 0]
    visited = set()
    latest: set[tuple[int, int]] = set()

    visited.add(start)
    latest.add(start)
    states[1] = 1

    state = 0
    for i in range(131):
        visited, latest = bfs(visited, latest)
        states[state] += len(latest)
        state = (state + 1) % 2
        print(i, max(states[0], states[1]))

    return max(states[0], states[1])


print(solve())