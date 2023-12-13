import difflib, frozenlist

data = open("i.txt").read()
lines = data.split("\n")

solutions: list[tuple[str, list[int], list[int]]] = []

m: dict[str, set[frozenlist.FrozenList[int]]] = dict()

def checkSolutions(solutions):
    for s in solutions:
        key = s[0] + str(s[1])
        if key not in m:
            m[key] = set()

        if s[2] in m[key]:
            print(f"Double entry: {s[0]} {s[1]} {s[2]}")
        m[key].add(s[2])
        # print(s)
        lastEnd = 0
        for n, i in zip(s[1], s[2]):
            if lastEnd < i-1:
                for k in range(lastEnd+1, i):
                    if s[0][k] == '#':
                        print(f"Unused #: {s[0]} {k} {s[1]} {s[2]}")
            lastEnd = i + n-1

            for j in range(n):
                if s[0][i + j] == '.':
                    print(f"Found wrong tile: {s[0]} at {i+j} {s[1]} {s[2]}")

        # print(s)
        for j in range(len(s[1])-1):
            if (s[2][j] + s[1][j] >= s[2][j+1]):
                print(f"Found overlap: {s[0]} at {s[2][j]}->{s[1][j]} X {s[2][j+1]}")

    




def tryPlace(string: str, nums, numIdx) -> tuple[int]:
    num = nums[numIdx]
    count = 0
    for i in range(len(string)-num+1):
        broken = False
        if i + num < len(string) and string[i + num] == '#':
            if string[i] == '#':
                break
            continue
        for j in range(num):
            if string[i + j] == '.':
                broken = True
                break
        if not broken:
            if numIdx == len(nums)-1:
                l = string.find('#', i + num)
                if l == -1:
                    count += 1
            else:
                count += tryPlace(string[i + num + 1:], nums, numIdx + 1)
        if string[i] == '#':
            break

    return count

def trySolveStr(tiles: str, nums: list[int]):
    return tryPlace(tiles, nums, 0)

count = 0

class Range:
    length: int = None
    mask: int = 0b0

    def __init__(self, input: str):
        self.length = len(input)
        i = 1
        for c in input:
            if c == '#':
                mask = mask & i
            i *= 2

    def tryPlacing(self, nums: list[int]):
        atMost = self.getAtMost(nums)    
        count = 0
        for  in nums[:atMost+1]:
            count += self.length - n + 1

        


for (ö, line) in enumerate(lines):
    tiles, nums = line.split(" ")
    tiles *= 5
    nums = [int(n) for n in nums.split(",")]
    nums *= 5

    rangeStrs = []
    start = 0
    current = 0
    while current < len(tiles):
        while current < len(tiles) and tiles[current] != '.':
            current += 1
        rangeStrs.append(tiles[start:current])
        while current < len(tiles) and tiles[current] !=  '.':
            current += 1
        start = current

    ranges =[Range(r) for r in rangeStrs]
    #print(tiles,nums)
    newCount = trySolveStr(tiles, nums)

    print(f"{ö+1}/{len(lines)}")

    #print(newCount)
    count += newCount

        


print(count)