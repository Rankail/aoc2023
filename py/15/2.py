data = open("i.txt").read()
lines = data.split(",")

boxes: dict[list[tuple[str, int]]] = {}

def hash(s: str) -> int:
    n = 0
    for c in s:
        asc = ord(c)
        n += asc
        n *= 17
        n %= 256

    return n

count = 0

def indexByLabel(box: list[tuple[str, int]], label: str) -> int:
    for i, lens in enumerate(box):
        if lens[0] == label:
            return i
    return -1

for line in lines:
    op = line.find('=')
    if op == -1:
        op = len(line)-1

    label = line[:op]
    box = hash(label)

    if box not in boxes:
        boxes[box] = []
    
    i = indexByLabel(boxes[box], label)
    if line[op] == '=':
        
        if i == -1:
            boxes[box].append((label, int(line[op+1:])))
        else:
            boxes[box][i] = (label, int(line[op+1:]))

    elif line[op] == '-' and i != -1:
        boxVal = boxes[box]
        if i == 0:
            boxVal = boxVal[1:]
        elif i == len(boxVal)-1:
            boxVal = boxVal[:-1]
        else:
            boxVal = boxVal[:i] + boxVal[i+1:]
        boxes[box] = boxVal

count = 0
for boxId, box in boxes.items():
    for pos, lens in enumerate(box):
        count += (boxId+1) * (pos+1) * lens[1]


print(count)