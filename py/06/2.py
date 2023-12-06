import bisect
import time as t

data = open("i.txt").read()
lines = data.split("\n")

races = []

count = 1
timeStr = ""
for timePart in lines[0][len("Time:"):].split(" "):
    timeStr += timePart.strip()

distStr = ""
for distPart in lines[1][len("Distance:"):].split(" "):
    distStr += distPart.strip()

time = int(timeStr)
dist = int(distStr)

# yes, i bruteforced it at first (runs in just over 1s)

# c = 0
# for i in range(1, time):
#     if (i * (time - i) > dist):
#         c = i
#         break

# the much faster way:
c = bisect.bisect(range(0, time // 2), dist, key = lambda x: x * (time-x))

count = time - c * 2 + 1

print(count)