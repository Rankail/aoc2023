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

def bfsParity(visited: set[tuple[int, int]], latest: set[tuple[int, int]]):
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

def calcQuadratic(factors, x):
    d0, d1, d2 = factors[0], factors[1] - factors[0], factors[2] - 2 * factors[1] + factors[0]
    return d0 + d1 * x + d2 * (x * (x - 1) // 2)

@profiler
def solve():
    factors = []
    p1answer = 0
    goalsteps = 26501365

    start = None
    for (y, line) in enumerate(lines):
        sIdx = line.find('S')
        if sIdx != -1:
            start = (sIdx, y)
            break

    visited = {start}
    newNodes = {start}

    counts = [0, 1]
    state = 0

    count = 1
    while True:
        visited, newNodes = bfsParity(visited, newNodes)
        counts[state] += len(newNodes)

        if count == 64:
            p1answer = counts[state]
        elif count % w == goalsteps % w:
            factors.append(counts[state])
            if len(factors) >= 3:
                return p1answer, calcQuadratic(factors, goalsteps // w)

        state = (state+1) % 2
        count += 1

print(solve())