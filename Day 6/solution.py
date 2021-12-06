with open("input.txt") as input:
    data = list(filter(lambda x: len(x), input.read().split("\n")))

fish = list(map(int,data[0].split(",")))
from collections import Counter, defaultdict

grid = Counter(fish)

days = 256
for d in range(days):
    temp = defaultdict(int)
    for key, val in grid.items():
        if key==0:
            temp[6] += val
            temp[8] += val
        else:
            temp[key-1] += val

    grid = temp

print(sum(grid.values()))