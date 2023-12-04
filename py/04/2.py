data = open("i.txt").read()
lines = data.split("\n")

copies = [1 for _ in range(len(lines))]
for (y, line) in enumerate(lines):
    _, g = line.split(": ")
    win, nums = g.split(" | ")
    ws = set()
    for num in win.split(" "):
        if (len(num.strip()) != 0):
            ws.add(int(num))

    n = 0
    for num in nums.split(" "):
        if (len(num.strip()) != 0 and int(num) in ws):
            n += 1

    if (n != 0):
        for i in range(1, n+1):
            copies[y + i] += copies[y]

print(sum(copies))