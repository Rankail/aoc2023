import time

def timeToStr(ns: int):
    units = [
        "ns", "µs", "ms", "s"
    ]

    text = ""

    i = 0
    while ns != 0:
        rest = ns % 1000
        if rest != 0:
            text = str(rest) + units[i] + " " + text
        ns //= 1000
        i += 1

    return text

data = open("i.txt").read()
lines = data.split("\n")

class Hand():
    hand: str = None
    bid: int = None
    strength: int = 0

    def __init__(self, input: str):
        self.hand, bid = input.split(" ")
        self.bid = int(bid)

        self.calcStrength()

    def calcStrength(self):
        m = dict()
        for c in self.hand:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1


        maxs = (sorted(m.values(), reverse = True)[:2])
        if "J" in m:
            js = m["J"]
            m["J"] = 0

            maxs = (sorted(m.values(), reverse = True)[:2])

            maxs[0] += js

        

        ranking = 0
        if (maxs[0] == 1):
            ranking = 1
        elif (maxs[0] == 2 and (len(maxs) > 1 and maxs[1] == 2)):
            ranking = 3
        elif (maxs[0] == 2):
            ranking = 2
        elif (maxs[0] == 3 and len(maxs) > 1 and maxs[1] == 2):
            ranking = 5
        elif (maxs[0] == 3):
            ranking = 4
        elif (maxs[0] == 4):
            ranking = 6
        elif (maxs[0] == 5):
            ranking = 7

        strength = 0
        factor = 1
        for c in reversed(self.hand):
            strength += factor * Hand.getValueOfCard(c)
            factor *= 15

        strength += ranking * factor
        self.strength = strength

    def getValueOfCard(c: str):
        if c.isdigit():
            return int(c)
        if c == "T": return 10
        if c == "J": return 0
        if c == "Q": return 12
        if c == "K": return 13
        if c == "A": return 14

        raise ValueError("Unexpected card")
    
    def __str__(self):
        return f"{self.hand} {self.strength} {self.bid}"
    
    def __repr__(self):
        return str(self)

startTime = time.perf_counter_ns()

hands: list[Hand] = []
for line in lines:
    hands.append(Hand(line))

hands.sort(key = lambda h: h.strength)

count = 0
for (i, h) in enumerate(hands):
    count += h.bid * (i+1)


endTime = time.perf_counter_ns()
print(f"Finished after {timeToStr(endTime - startTime)}")

print(count)