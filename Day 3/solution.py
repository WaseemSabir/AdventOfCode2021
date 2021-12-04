with open("input.txt","r") as input:
    data = list(filter(lambda x: len(x),input.read().split("\n")))

## Part 1
print("Part 1")
def binary_str_to_decimal(ms):
    decimal = 0
    for i, num in enumerate(ms[::-1]):
        num = int(num)
        if num:
            decimal += pow(2, i)

    return decimal

splited = []
for i in range(len(data[0])):
    splited.append([int(s[i]) for s in data])

gemma = ""
epsilon = ""

for lis in splited:
    most_common = 1 if sum(lis)>=len(lis)/2 else 0
    least_common = 0 if sum(lis)>=len(lis)/2 else 1

    gemma += str(most_common)
    epsilon += str(least_common)

gemma_d = binary_str_to_decimal(gemma)
epsilon_d = binary_str_to_decimal(epsilon)

print(f"Gemma: {gemma_d}")
print(f"Epsilon: {epsilon_d}")
print(f"Solution: {gemma_d*epsilon_d}")

## Part 2
def convert_to_splited(o_data):
    splited = []
    for i in range(len(o_data[0])):
        splited.append([int(s[i]) for s in o_data])

    return splited


tracking_o = data
tracking_co = data

print()
print("Part 2")
for index in range(len(data[0])):
    lis_o = convert_to_splited(tracking_o)[index]
    most_common = 1 if sum(lis_o)>=len(lis_o)/2 else 0

    lis_co = convert_to_splited(tracking_co)[index]
    least_common = 0 if sum(lis_co)>=len(lis_co)/2 else 1

    if len(tracking_o)>1:
        temp_o = tracking_o
        tracking_o = []

        for bin in temp_o:
            if bin[index]==str(most_common):
                tracking_o.append(bin)

    if len(tracking_co)>1:
        temp_co = tracking_co
        tracking_co = []

        for bin in temp_co:
            if bin[index]==str(least_common):
                tracking_co.append(bin)

o = binary_str_to_decimal(tracking_o[0])
co = binary_str_to_decimal(tracking_co[0])

print(f"O: {o}")
print(f"CO: {co}")
print(f"Solution: {co*o}")