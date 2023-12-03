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
            
        if len(m.keys()) > 3 or not (cc(m, "red", 12) and cc(m, "green", 13) and cc(m, "blue", 14)):
            print(game)
            broken = True

    if not broken:
        count += game

print(count)
        