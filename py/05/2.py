from collections import deque

data = open("i.txt").read()
lines = data.split("\n")

sections = data.split("\n\n")[1:]

class CopyRange:
    srcStart = 0
    dstStart = 0
    length = 0

    def __init__(self, src, dst, length):
        self.srcStart = src
        self.dstStart = dst
        self.length = length

    def __str__(self):
        return f"({self.srcStart}-{self.srcStart+self.length})->{self.dstStart}"
    
    def __repr__(self):
        return str(self)

class Range:
    start = 0
    length = 0

    def __init__(self, start, length):
        self.start = start
        self.length = length

    def __str__(self):
        return f"({self.start}-{self.start+self.length})"
    
    def __repr__(self):
        return str(self)
    
    def splitEndOff(self, end):
        nr = Range(end, self.start + self.length - end)
        self.length = end - self.start
        print(f"split at {end}: ({self.start}-{self.start + self.length + nr.length})->{self} {nr}")
        return nr
    
    def splitStartOff(self, start):
        br = Range(self.start, start - self.start)
        self.length -= (start - self.start)
        self.start = start
        print(f"split at {start}: ({br.start}-{br.start + self.length + br.length})->{br} {self}")
        return br

currentState: deque[Range] = deque()
initialNums = [int(n) for n in lines[0].split(": ")[1].split(" ")]
for i in range(0, len(initialNums), 2):
    currentState.append(Range(initialNums[i], initialNums[i+1]))

print(sum(s.length for s in currentState), len(currentState))

for section in sections:
    ranges: list[CopyRange] = []
    for line in section.split("\n")[1:]:
        dst, src, length = [int(n) for n in line.split(" ")]
        ranges.append(CopyRange(src, dst, length))

    ranges.sort(key=lambda r: r.srcStart)

    prevLen = sum(s.length for s in currentState)

    nextState: deque[Range] = deque()
    while (len(currentState) != 0):
        sr = currentState.popleft()
        found = False
        i = 0
        if (sr.start + sr.length < ranges[0].srcStart):
            i = len(ranges)

        while i < len(ranges):
            r = ranges[i]
            # recipe ----------|
            # seeds            |-------------
            if r.srcStart + r.length <= sr.start:
                i += 1
                continue

            # recipe           |-------------
            # seeds   ---------|
            if r.srcStart > sr.start + sr.length:
                nextState.append(sr)
                break
            
            # recipe ----------|
            # seeds  ----------|-------------
            if (sr.start + sr.length >= r.srcStart + r.length):
                nr = sr.splitEndOff(r.srcStart + r.length)
                print("added additional range")
                currentState.append(nr)

            # recipe           |-------------
            # seeds  ----------|-------------
            if (sr.start < r.srcStart):
                nr = sr.splitStartOff(r.srcStart)
                nextState.append(nr)

            found = True
            print("transformed range")
            nextState.append(Range(sr.start + (r.dstStart - r.srcStart), sr.length))
            break
        
        if (i == len(ranges)):
            print("copied defaulted range")
            nextState.append(sr)
        
    newLen = sum(s.length for s in nextState)
    print(prevLen, newLen, len(nextState), "\n\n")
    
    currentState = nextState

print(sum(s.length for s in currentState), len(currentState))

print(min(s.start for s in currentState))