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

class Range:
    start: int = None
    end: int = None
    y: int = None

    def __init__(self, start, end, y):
        self.start = start
        self.end = end
        self.y = y

    def __lt__(self, other):
        if self.start != other.start:
            return self.start < other.start
        
        return self.y < other.y
    
    def split(self, splits: list[int]):
        ranges = []
        for x in splits:
            if self.start <= x <= self.end:
                if self.start != x:
                    ranges.append(Range(self.start, x, self.y))
                self.start = x

        if self.start != self.end:
            ranges.append(self)

        return ranges
    
    def __str__(self):
        return f"({self.start} - {self.end} ;{self.y})"
    
    def __repr__(self):
        return self.__str__()


class Section:
    startX: int = None
    endX: int = None
    ys: list[int] = None

    def __init__(self, startX, endX, ys):
        self.startX = startX
        self.endX = endX
        self.ys = ys

    def fromRanges(ranges: list[Range]):
        sections = []
        startI = 0
        currentI = startI
        while currentI < len(ranges):
            currentI = startI
            while currentI < len(ranges) and ranges[currentI].start == ranges[startI].start:
                currentI += 1

            ys = [r.y for r in ranges[startI:currentI]]
            sections.append(Section(ranges[startI].start, ranges[startI].end, ys))
            
            startI = currentI

        return sections
    
    def __str__(self):
        return f"({self.startX} - {self.endX} ; {self.ys})"
    
    def __repr__(self):
        return self.__str__()
        


def getDirOfChar(c):
    if c == 'D': return (0,1)
    if c == 'U': return (0,-1)
    if c == 'L': return (-1,0)
    if c == 'R': return (1,0)
    return None

def getDirOfIdx(i):
    if i == 0: return (1,0)
    if i == 1: return (0,1)
    if i == 2: return (-1,0)
    if i == 3: return (0,-1)
    return None

def splitRanges(ranges: list[Range], splits: set[int]):
    newRanges = []
    for r in ranges:
        nr = r.split(splits)
        newRanges.extend(nr)

    return newRanges


count = 0
def parseDigger(lines: list[str]):
    curPos = (0,0)
    ranges = []
    splits = set()

    circ = 0

    for line in lines:
        dirChar, length, _ = line.split(" ")
        length = int(length)
        circ += length
        
        dx, dy = getDirOfChar(dirChar)
        if dx == 0:
            splits.add(curPos[0])
        elif dy == 0:
            x1 = curPos[0]
            x2 = curPos[0] + dx * length
            ranges.append(Range(min(x1, x2), max(x1, x2), curPos[1]))

        curPos = (curPos[0] + dx * length, curPos[1] + dy * length)

    splits = sorted(list(splits))

    return ranges, splits, circ

def calculateInnerArea(sections: list[Section]):
    area = 0
    for section in sections:
        for i in range(0, len(section.ys), 2):
            y1 = section.ys[i]
            y2 = section.ys[i+1]
            size = (y2 - y1 - 1) * (section.endX - section.startX - 1)
            area += size

    for i in range(0, len(sections)-1):
        p = sections[i]
        n = sections[i+1]
        for j in range(0, len(p.ys), 2):
            for k in range(0, len(n.ys), 2):
                start = max(p.ys[j], n.ys[k])
                end = min(p.ys[j+1], n.ys[k+1])
                if start > end:
                    continue

                area += end - start-1

    return area

@profiler
def solve():
    m: dict[tuple[int, int], int] = dict()

    ranges, splits, circ = parseDigger(lines)
    ranges = splitRanges(ranges, splits)
    ranges.sort()

    sections = Section.fromRanges(ranges)

    area = calculateInnerArea(sections)

    return area + circ

print(solve())
# 94_117_869_444_567

#  0123456
# 0#######0
# 1#.....#1
# 2###...#2
# 3..#...#3
# 4..#...#4
# 5###.###5
# 6#...#..6
# 7##..###7
# 8.#....#8
# 9.######9
