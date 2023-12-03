data = open("i.txt").read()
lines = data.split("\n")

def cc(m: dict[str, int], color: str, num: int)-> bool:
    return  (color not in m) or m[color] <= num

count = 0
for (i, line) in enumerate(lines):

    d = line.split(": ")
    game = d[0]
    game = int(game.split(" ")[1])
    d = d[1]
    broken = False
    ma = dict()
    for e in d.split("; "):
        if broken: break
        m = dict()
        for c in e.split(", "):
            #print(c)
            o = c.split(" ")
            num = int(o[0])
            col = o[1]
            if not(col in m):
                m[col] = num
            else:
                m[col] += num
        for (k, v) in m.items():
            if k in ma:
                if ma[k] < v:
                    ma[k] = v
            else:
                ma[k] = v

    power = 1
    for v in ma.values():
        power *= v

    print(power)
    count += power

print(count)
        