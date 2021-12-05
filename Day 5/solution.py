with open("input.txt") as input:
    data = list(filter(lambda x: len(x), input.read().split("\n")))

broken = list(map(lambda x: x.split(" -> "), data))

# Part 1
all_points = []

for one in broken:
    x1, y1 = list(map(int, one[0].split(",")))
    x2, y2 = list(map(int, one[1].split(",")))
    
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                all_points.append((x,y))

from collections import Counter
interset = 0

counts = Counter(all_points)
for val in counts:
    if counts[val]>1:
        interset+=1

print(interset)

# Part 2
all_points = []

for one in broken:
    x1, y1 = list(map(int, one[0].split(",")))
    x2, y2 = list(map(int, one[1].split(",")))
    
    dx = x2 - x1
    dy = y2 - y1
    if dx:
        dx = dx // abs(dx)
    if dy:
        dy = dy // abs(dy)

    x = x1
    y = y1
    while True:
        all_points.append((x, y))
        if x == x2 and y == y2:
            break
        x += dx
        y += dy

interset = 0

counts = Counter(all_points)
for val in counts:
    if counts[val]>1:
        interset+=1

print(interset)