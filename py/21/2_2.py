data = open("i.txt").read()
lines = data.split("\n")

w = len(lines[0])
h = len(lines)

def bfs(visited: set[tuple[int, int]], latest: set[tuple[int, int]]):
    newFound: set[tuple[int, int]] = set()

    for x, y in latest:
        for dx, dy in ((-1, 0), (0,-1), (1,0), (0,1)):
            nx = x + dx
            ny = y + dy
            if (nx, ny) in visited: continue
            if lines[ny % h][nx % w] == "#": continue

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

    target = 26501365
    blocks = target / w
    remainder = target % w
    
    values = []

    state = 0
    for i in range(2 * w + remainder+3):
        visited, latest = bfs(visited, latest)
        states[state] += len(latest)
        state = (state + 1) % 2
        if ((i-remainder+2) % w == 0):
            values.append(max(states[0], states[1]))

    print(values)

    c = values[0]
    ab = values[1] - c
    a4b2 = values[2] - c
    a2 = a4b2 - 2 * ab
    a = a2 / 2
    b = ab - a

    return a * (blocks ** 2) + b * blocks + c


print(solve())