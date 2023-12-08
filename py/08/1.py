data = open("i.txt").read()
lines = data.split("\n")

m = dict()

lr = lines[0]
lines = lines[2:]

cur = "AAA"
count = 0
for line in lines:
    fromPos, toPos = line.split(" = ")
    left, right = toPos[1:-1].split(", ")
    m[fromPos] = (left, right)


i = 0
while (cur != "ZZZ"):
    instruction = 0 if lr[i % len(lr)] == "L" else 1
    cur = m[cur][instruction]
    i += 1

print(i)