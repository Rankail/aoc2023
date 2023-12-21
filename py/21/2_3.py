data = open("i.txt").read()
lines = data.split("\n")

def solve():
    Factors, nextfactor, p1answer, p2answer, goalsteps, Pos, dirs = [0, 0, 0], 0, 0, 0, 26501365, {Startpos}, [(1, 0),(0, 1), (-1, 0) ,(0, -1)]
    for count in range(1, 1000):
        npos = set()
        for r, c in Pos:
            for dirn in dirs:
                nr, nc = r + dirn[0], c + dirn[1]
                if Grid[nr % Rows][nc % Cols] != "#":
                    npos.add((nr, nc))
        Pos = npos
        if count == 64:
            p1answer = len(Pos)
        elif count % Rows == goalsteps % Rows:
            Factors[nextfactor] = len(Pos)
            nextfactor += 1
            if nextfactor == 3:
                delta0, delta1, delta2 = Factors[0], Factors[1] - Factors[0], Factors[2] - 2 * Factors[1] + Factors[0]
                p2answer = delta0 + delta1 * (goalsteps // Rows) + delta2 * ((goalsteps // Rows) * ((goalsteps // Rows) - 1) // 2)
                return p1answer, p2answer

Grid = [[char for char in line] for line in lines]
Rows, Cols, Startpos = len(Grid), len(Grid[0]), (0, 0)
for row in range(Rows):
    col = lines[row].rfind('S')
    if col > -1:
        Startpos = (row, col)
        Grid[row][col] = '.'
print(solve())