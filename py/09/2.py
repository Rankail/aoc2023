data = open("i.txt").read()
lines = data.split("\n")

def testZero(arr: list[int]):
    for n in arr:
        if n != 0: return False
    return True

def diffs(arr: list[int]):
    diff = []
    for i in range(0, len(arr)-1):
        diff.append(arr[i+1] - arr[i])

    return diff

def interpolate(nums: list[int]):
    arrs = [nums]

    while not testZero(arrs[-1]):
        arrs.append(diffs(arrs[-1]))

    for i in range(len(arrs)-2, -1, -1):
        arrs[i].insert(0, arrs[i][0] - arrs[i+1][0])

    return arrs[0]

count = 0    
for line in lines:
    nums = [int(n) for n in line.split(" ")]
    nums = interpolate(nums)
    count += nums[0]

print(count)




