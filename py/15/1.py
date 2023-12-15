data = open("i.txt").read()
lines = data.split(",")

def hash(s: str) -> int:
    n = 0
    for c in s:
        asc = ord(c)
        n += asc
        n *= 17
        n %= 256

    return n

count = 0
for line in lines:
    count += hash(line)

print(count)