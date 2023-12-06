import bisect
import time as t

data = open("i.txt").read()
lines = data.split("\n")

races = []

for time in lines[0][len("Time:"):].split(" "):
    if (len(time.strip()) != 0):
        races.append([int(time)])

i = 0
for time in lines[1][len("Distance:"):].split(" "):
    if (len(time.strip()) != 0):
        races[i].append(int(time))
        i += 1

count = 1
for race in races:
    # c = 0
    # for i in range(1, race[0]):
    #     if (i * (race[0] - i) > race[1]):
    #         c += 1

    c = bisect.bisect(range(0, race[0] // 2), race[1], key = lambda x: x * (race[0] - x))

    count *= race[0] - 2 * c + 1

print(count)