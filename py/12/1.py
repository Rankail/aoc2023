import difflib, frozenlist

data = open("i2.txt").read()
lines = data.split("\n")

# class Tile:
#     type: str = None
#     length: int = None

#     def __init__(self, type, length):
#         self.type = type
#         self.length = length


# class Range:
#     length: int = None
#     earliest: int = None
#     latest: int = None

#     def __init__(self, length, earliest = None, latest = None):
#         self.length = length
#         self.earliest = earliest
#         self.latest = latest

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

    




def tryPlace(string: str, nums, numIdx, fullS, idx, path: list[int]) -> int:
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
                    fl = frozenlist.FrozenList(path.copy() + [idx+i])
                    print(path.copy() + [idx+i])
                    fl.freeze()
                    solutions.append((fullS, nums, fl))
                    count += 1
            else:
                count += tryPlace(string[i + num + 1:], nums, numIdx + 1, fullS, idx + i + num + 1, path + [idx + i])
        if string[i] == '#':
            break

    return count

def trySolveStr(tiles: str, nums: list[int]):
    return tryPlace(tiles, nums, 0, tiles, 0, [])
    
    

    



# def trySolve(tiles: list[Tile], ranges: list[Range]):
#     j = 0
#     for i, r in enumerate(ranges):
#         while (tiles[j] == '.'):
#             j += 1
        
#         needed = r.length
#         if (tiles[j].type == '?'):
#             if tiles[j].length > needed + 1:
                
#             elif tiles[j].length < needed:


#print(trySolveStr("?#?##..??##??##", [1, 2, 3, 2]))
newData = ""
count = 0

for line in lines[-1:]:
    tiles, nums = line.split(" ")
    # tiles *= 5
    # nums = [int(n) for n in nums.split(",")]
    # nums *= 5

    tiles = "?###????????"

    nums = [5, 2, 1]


    #print(tiles,nums)
    newCount = trySolveStr(tiles, nums)

    #print(newCount)
    count += newCount

    newLine = tiles + " " + ",".join(str(n) for n in nums) + "\n"
    newData += newLine



checkSolutions(solutions)
        


print(count)
# high 8206
# high 7961
# high 7879
# probably low 518
# maybe 7361