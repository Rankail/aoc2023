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

data = open("i.txt").read()
lines = data.split("\n")

modules: dict[str, tuple[str, str]] = dict()
destinations: dict[str, list[str]] = dict()

memories: dict[str, dict[str, bool]] = dict()
switches: dict[str, bool] = dict()

def parse():
    global modules, destinations, memories, switches
    modules = dict()
    destinations = dict()

    memories = dict()
    switches = dict()

    for line in lines:
        module, dests = line.split(" -> ")
        moduleName = module[1:]
        moduleType = module[0]

        dests = dests.split(", ")

        if moduleType == '%':
            modules[moduleName] = (moduleName, moduleType)
        elif moduleType == '&':
            modules[moduleName] = (moduleName, moduleType)
        else:
            moduleName = module
            modules[moduleName] = (moduleName, '')
        
        switches[moduleName] = False
        memories[moduleName] = dict()
        destinations[moduleName] = dests


    for name, dests in destinations.items():
        for d in dests:
            if not d in memories:
                memories[d] = dict()
            memories[d][name] = False

def pressButton(q: deque[str]):
    global memories, switches, destinations, modules
    low = 1
    high = 0

    while q:
        source, pulseIn, target = q.popleft()

        if target not in modules: continue

        moduleName, moduleType = modules[target]

        pulseOut = False



        if moduleType == '':
            pulseOut = pulseIn
        elif moduleType == '%':
            if pulseIn == 1:
                continue
            pulseOut = not switches[moduleName]
            switches[moduleName] = pulseOut
        elif moduleType == '&':
            memories[moduleName][source] = pulseIn
            pulseOut = not all(m for m in memories[moduleName].values())

        if pulseOut:
            high += len(destinations[moduleName])
        else:
            low += len(destinations[moduleName])

        for d in destinations[moduleName]:
            # print(f"{target} {'high' if pulse else 'low'} -> {d}")
            q.append((moduleName, pulseOut, d))

    return low, high

@profiler
def solve():
    parse()

    q: deque[tuple[bool, str]] = deque()
    q.append(("", False, "broadcaster"))

    #count = 0
    low = 0
    high = 0
    
    for _ in range(1000):
        nl, nh = pressButton(q.copy())
        low += nl
        high += nh
        print(high, low)
        print()

    print(high, low)

    return high * low

print(solve())