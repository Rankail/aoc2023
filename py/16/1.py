from collections import deque

data = open("i.txt").read()
lines = data.split("\n")

width = len(lines[0])
height = len(lines)

def getDir(dir: int)-> tuple[int, int]:
    if dir == 0:
        return (-1,0)
    if dir == 1:
        return (0,-1)
    if dir == 2:
        return (1,0)
    if dir == 3:
        return (0,1)
    
    raise ValueError("Wront direction value")

def mirrorDir(dir, mirrorChar):
    if mirrorChar == '/':
        if dir == 0:
            return 3
        if dir == 1:
            return 2
        if dir == 2:
            return 1
        if dir == 3:
            return 0
    if mirrorChar == '\\':
        if dir == 0:
            return 1
        if dir == 1:
            return 0
        if dir == 2:
            return 3
        if dir == 3:
            return 2
        
    return dir

def addPosByDir(q: deque, x, y, dir):
    dx, dy = getDir(dir)
    nx = x + dx
    ny = y + dy
    if nx < 0 or ny < 0 or nx >= width or ny >= height: return
    q.append((nx, ny, dir))

def computeState(q: deque[tuple[int, int, int]], states: set[tuple[int, int, int]], state):
    if state in states: return
    states.add(state)
    curTile = lines[state[1]][state[0]]
    dir = state[2]
    dir = mirrorDir(dir, curTile)
    
    x, y = state[0], state[1]

    if curTile == '|' and dir % 2 == 0:
        addPosByDir(q, x, y, (dir+1)%4)
        addPosByDir(q, x, y, (dir+3)%4)
    elif curTile == '-' and dir % 2 == 1:
        addPosByDir(q, x, y, (dir+1)%4)
        addPosByDir(q, x, y, (dir+3)%4)
    else:
        addPosByDir(q, x, y, dir)

q: deque[tuple[int, int, int]] = deque()
states = set()
q.append((0, 0, 2))

while len(q) != 0:
    state = q.popleft()
    computeState(q, states, state)

energized = set()
for state in states:
    energized.add((state[0], state[1]))

print(len(energized))