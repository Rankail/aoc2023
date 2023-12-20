from __future__ import annotations
import time
from collections import deque
import itertools

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.perf_counter()
        ret = method(*arg, **kw)
        print("Method " + method.__name__ + " took : " + "{:2.5f}".format(time.perf_counter() - t) + " sec")
        return ret

    return wrapper_method

data = open("i5.txt").read()
lines = data.split("\n")

modules: dict[str, Module] = dict()

class Module:
    name: str = None
    destinations: list[str]

    def receive(self, pulse: bool) -> list[tuple[str, bool]]:
        pass

    def send(self, modules: dict[str, Module]):
        pass

    def getState(self):
        pass

class FlipFlop(Module):
    state: bool = False
    sending: bool = False

    def receive(self, pulse: bool) -> list[tuple[str, bool]]:
        if pulse == False:
            self.state = not self.state
            self.sending = True
        else:
            self.sending = False

    def send(self):
        global modules
        if not self.sending:
            return None
        return self.state
        
    def getState(self):
        return self.state

    def __str__(self):
        return f"{self.name} ({1 if self.state else 0}) -> {', '.join(self.destinations)}"
    
    def __repr__(self):
        return str(self)

class Conjunction(Module):
    inputs: list[str]= None

    def setup(self, inputs: list[str]):
        self.inputs = inputs

    def receive(self, pulse: bool) -> list[tuple[str, bool]]:
        pass
        
    def send(self):
        global modules
        high = True
        for i in self.inputs:
            if not modules[i].getState():
                high = False
                break

        return not high
    
    def __str__(self):
        t = tuple((1 if modules[i].getState() else 0) for i in self.inputs)
        return f"{self.name} {t}-> {', '.join(self.destinations)}"
    
    def __repr__(self):
        return str(self)


def parse():
    global modules
    starts = None
    modules = dict()
    inputMap: dict[str, list[str]] = dict()
    for line in lines:
        module, dests = line.split(" -> ")
        moduleName = module[1:]
        moduleType = module[0]

        dests = dests.split(", ")

        if moduleType == '%':
            module = FlipFlop()
        elif moduleType == '&':
            module = Conjunction()
        elif module == "broadcaster":
            starts = dests
            continue

        for d in dests:
            if d not in inputMap:
                inputMap[d] = []
            inputMap[d].append(moduleName)

        module.name = moduleName
        module.destinations = dests

        modules[moduleName] = module


    for n, m in modules.items():
        if isinstance(m, Conjunction):
            m.setup(inputMap[n])

    return starts

def pressButton(q: deque[str]):
    low = 1
    high = 0

    low += len(q)

    for s in q:
        modules[s].receive(False)
        print(f"broadcaster low -> {s}")

    q.append(None)

    pulseQ: deque[tuple[bool, str]] = deque()

    while len(q) > 1:
        target = q.popleft()

        if target == None:
            q.append(None)
            while pulseQ:
                p, t = pulseQ.popleft()
                if t in modules:
                    modules[t].receive(p)
            
            continue

        if target == "output":
            continue

        #print(f"{source} -{1 if pulse else 0}> {target}")

        if target not in modules: continue  
        m = modules[target]
        pulse = m.send()

        if pulse == None:
            continue

        if pulse:
            high += len(m.destinations)
        else:
            low += len(m.destinations)

        for d in m.destinations:
            print(f"{target} {'high' if pulse else 'low'} -> {d}")
            if d != "output":
                pulseQ.append((pulse, d))

        q.extend(m.destinations)

    return low, high

@profiler
def solve():
    starts = parse()

    q: deque[str] = deque()
    for start in starts:
        q.append(start)

    #count = 0
    low = 0
    high = 0
    
    for _ in range(2):
        nl, nh = pressButton(q.copy())
        low += nl
        high += nh
        print(high, low)
        print()

    print(high, low)

    return high * low

print(solve())
# 816928356 low