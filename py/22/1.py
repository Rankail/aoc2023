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

def parseCoord(s: str):
    s = s.split(",")
    return int(s[0]), int(s[1]), int(s[2])

def parse():
    bricks = []
    for line in lines:
        tlu, brd = line.split("~")
        tlu = parseCoord(tlu)
        brd = parseCoord(brd)
        bricks.append((tlu, brd))

    return bricks

def brickToParts(brick: tuple[tuple[int, int, int], tuple[int, int, int]]):
    diff = -1
    for i in range(3):
        if brick[0][i] != brick[1][i]:
            diff = i

    parts = []
    for i in range(brick[0][diff], brick[1][diff]+1):
        part = tuple(v if j != diff else i for j, v in enumerate(brick[0]))
        parts.append(part)

    return parts

def getSupportsForBricks(bricks):
    heap = []

    # work bottom->up with min-heap
    id = 0
    for brick in bricks:
        heappush(heap, (brick[0][2], id, brick))
        id += 1

    surrounding: dict[tuple[int, int, int], int] = dict()
    supportedBy: dict[int, set[int]] = dict()

    while heap:
        _, id, brick = heappop(heap)

        parts = brickToParts(brick)


        z = parts[0][2]
        support = set()
        # only need to check one block
        if len(parts) == 1 or parts[1][2] != z:
            while z > 0:
                z -= 1
                coord = (parts[0][0], parts[0][1], z)
                if coord in surrounding:
                    support.add(surrounding[coord])
                    z += 1
                    break
        # check line
        else:
            while z > 0:
                z -= 1
                for part in parts:
                    coord = (part[0], part[1], z)
                    if coord in surrounding:
                        support.add(surrounding[coord])

                if support:
                    z += 1
                    break


        for part in parts:
            surrounding[(part[0], part[1], z + part[2] - parts[0][2])] = id

        supportedBy[id] = support

    return supportedBy

@profiler
def solve():
    bricks = parse()

    supportedBy = getSupportsForBricks(bricks)

    count = 0

    needed = set()

    for i in range(len(bricks)):
        if len(supportedBy[i]) == 1:
            needed.add(supportedBy[i].pop())

    count = len(bricks) - len(needed)

    return count



print(solve())