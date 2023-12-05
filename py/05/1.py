data = open("i.txt").read()
lines = data.split("\n")

sections = data.split("\n\n")[1:]

class Range:
    srcStart = 0
    dstStart = 0
    length = 0

    def __init__(self, src, dst, length):
        self.srcStart = src
        self.dstStart = dst
        self.length = length

currentState = [int(n) for n in lines[0].split(": ")[1].split(" ")]

for section in sections:
    ranges: list[Range] = []
    for line in section.split("\n")[1:]:
        dst, src, length = [int(n) for n in line.split(" ")]
        ranges.append(Range(src, dst, length))

    nextState: list[int] = []
    for num in currentState:
        found = False
        for r in ranges:
            if r.srcStart > num: continue
            if r.srcStart + r.length <= num: continue
            found = True
            nextState.append(num + (r.dstStart - r.srcStart))
        
        if (not found):
            nextState.append(num)
    
    currentState = nextState

print(min(currentState))