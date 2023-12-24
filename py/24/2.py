from z3 import Solver, Int, BitVec, Real
import time

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.perf_counter()
        ret = method(*arg, **kw)
        print("Method " + method.__name__ + " took : " + "{:2.5f}".format(time.perf_counter() - t) + " sec")
        return ret

    return wrapper_method

test = False
if test:
    data = open("i2.txt").read()
    areaStart =  7
    areaEnd   = 27
else:
    data = open("i.txt").read()
    areaStart = 200000000000000
    areaEnd   = 400000000000000
lines = data.split("\n")

def parseCoord(s: str):
    s = s.split(",")
    return int(s[0]), int(s[1]), int(s[2])

def parse():
    hails = []
    for line in lines:
        pos, vel = line.split("@")
        pos = parseCoord(pos)
        vel = parseCoord(vel)
        hails.append((pos, vel))
    return hails

@profiler
def solve():
    hails = parse()

    #I = lambda name: Int(name)
    #I = lambda name: BitVec(name, 64)
    I = lambda name: Real(name)

    x, y, z = I("x"), I("y"), I("z")
    vx, vy, vz = I("vx"), I("vy"), I("vz")

    solver = Solver()

    for i, hail in enumerate(hails[:3]):
        (px, py, pz), (pvx, pvy, pvz) = hail

        t = I(f"t{i}")
        solver.add(t >= 0)
        solver.add(x + vx * t == px + pvx * t)
        solver.add(y + vy * t == py + pvy * t)
        solver.add(z + vz * t == pz + pvz * t)

    print(solver.check())

    model = solver.model()
    rx, ry, rz = model.eval(x).as_long(), model.eval(y).as_long(), model.eval(z).as_long()

    return rx + ry + rz

print(solve())