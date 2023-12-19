from collections import deque

data = open("i.txt").read()
lines = data.split("\n")

class Compare:
    var: str = None
    value: int = None
    typ: str = None# < > .
    target: str = None

    def __str__(self):
        if self.typ == '.': return f"-> {self.target}"
        return f"{self.var} {self.typ} {self.value} -> {self.target}"
    
    def __repr__(self):
        return str(self)
    
    def compare(self, value: dict[str, int]) -> tuple[bool, str]:
        if self.typ == '<':
            if value[self.var] < self.value: return True, self.target
            return False, None
        if self.typ == '>':
            if value[self.var] > self.value: return True, self.target
            return False, None
        if self.typ == '.':
            return True, self.target
        
        raise ValueError(f"Unknown operator {self.typ}")

class Workflow:
    name: str
    compares: list[Compare]

    def getNextTarget(self, v: dict[str, int]):
        for c in self.compares:
            worked, target = c.compare(v)
            if worked: return target
        
        raise ValueError("Expected 'else' statement")

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

def solve():
    ws, vs = parseData()

    q: deque[tuple[str, dict[str, int]]] = deque()
    for v in vs:
        q.append(("in", v))

    count = 0

    while q:
        wName, v = q.popleft()

        w = ws[wName]

        t = w.getNextTarget(v)

        if t == "R":
            pass
        elif t == "A":
            for val in v.values():
                count += val
        else:
            q.append((t, v))
        

    return count

print(solve())