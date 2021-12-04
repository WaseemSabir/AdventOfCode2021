with open("input.txt","r") as input:
    data = list(filter(lambda x: len(x),input.read().split("\n")))

# Part 1
global axis
axis = [0,0]

def input_map(str1, num):
    global axis
    if str1=="forward":
        axis[0]+=num
    elif str1=="down":
        axis[1]+=num
    elif str1=="up":
        axis[1]-=num

for line in data:
    s, n = line.split(" ")
    n = int(n)
    input_map(s, n)

print(axis[0]*axis[1])


## Part 2
global part2
part2 = [0, 0, 0] # Horizontal, depth, aim

def input_map(str1, num):
    global part2
    if str1=="forward":
        part2[0]+=num
        part2[1]+=part2[2]*num
    elif str1=="down":
        part2[2]+=num
    elif str1=="up":
        part2[2]-=num

for line in data:
    s, n = line.split(" ")
    n = int(n)
    input_map(s, n)

print(part2[0]*part2[1])