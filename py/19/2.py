from collections import deque
import copy

data = open("i.txt").read()
lines = data.split("\n")

class Range:
    start: int = None
    end: int = None

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def isValid(self):
        return self.start <= self.end
    
    def __str__(self):
        return f"({self.start} - {self.end})"
    
    def __repr__(self):
        return str(self)

class Compare:
    var: str = None
    value: int = None
    typ: str = None # < > .
    target: str = None

    def __str__(self):
        if self.typ == '.': return f"-> {self.target}"
        return f"{self.var} {self.typ} {self.value} -> {self.target}"
    
    def __repr__(self):
        return str(self)
    
    def compare(self, value: dict[str, Range]) -> tuple[tuple[str, dict[str, Range]], dict[str, Range]]: # 
        if self.typ == '<':
            goodRange = copy.deepcopy(value)
            goodRange[self.var].end = min(goodRange[self.var].end, self.value-1)
            value[self.var].start = max(value[self.var].start, self.value)
            return (self.target, goodRange), value
            
        if self.typ == '>':
            goodRange = copy.deepcopy(value)
            goodRange[self.var].start = max(goodRange[self.var].start, self.value+1)
            value[self.var].end = min(value[self.var].end, self.value)
            return (self.target, goodRange), value
            
        if self.typ == '.':
            return (self.target, value), None
        
        raise ValueError(f"Unknown operator {self.typ}")

class Workflow:
    name: str
    compares: list[Compare]

    def getNextTarget(self, ranges: dict[str, Range]):
        done: list[tuple[str, dict[str, Range]]] = []

        for c in self.compares:
            (target, goodRange), ranges = c.compare(ranges) # ranges = rest
            if all(r.isValid() for r in goodRange.values()):
                done.append((target, goodRange))
            if ranges == None: break

        return done

    def __str__(self):
        return f"{self.name} {self.compares}"
    
    def __repr__(self):
        return str(self)

def parseCompare(s: str) -> Compare:
    c = Compare()
    if s.find(':') != -1:
        r, c.target = s.split(":")
        c.var = r[0]
        c.typ = r[1]
        c.value = int(r[2:])
        
    else:
        c.typ = '.'
        c.target = s
        c.value = None
        c.var = None

    return c


def parseWorkflow(s: str) -> tuple[str, Workflow]:
    w = Workflow()

    name, compares = s.split("{")
    w.name = name
    w.compares = [parseCompare(cs) for cs in compares[:-1].split(",")]
    
    return name, w

def parseValue(s: str) -> dict[str, int]:
    s = s.replace("{", "{\"").replace("=", "\":").replace(",", ",\"")
    return eval(s)

def parseData():
    workflowsStr, valuesStr = data.split("\n\n")

    workflowStrs = workflowsStr.split("\n")

    valueStrs = valuesStr.split("\n")

    workflows: dict[str, Workflow] = dict()
    for w in workflowStrs:
        wName, wObj = parseWorkflow(w) 
        workflows[wName] = wObj

    values = [parseValue(v) for v in valueStrs]

    return workflows, values


def createInitialRanges():
    return {
        "x": Range(1, 4000),
        "m": Range(1, 4000),
        "a": Range(1, 4000),
        "s": Range(1, 4000)
    }

def solve():
    ws, _ = parseData()

    ranges = createInitialRanges()

    accepted: list[dict[str, Range]] = []

    q: deque[tuple[str, dict[str, int]]] = deque()
    q.append(("in", ranges))

    while q:
        wName, v = q.popleft()

        w = ws[wName]

        res = w.getNextTarget(v)

        for (t, r) in res:
            if t == "R":
                pass
            elif t == "A":
                accepted.append(r)
            else:
                q.append((t, r))

    count = 0

    for a in accepted:
        comb = 1
        for r in a.values():
            comb *= r.end - r.start + 1
        count += comb

    return count

print(solve())