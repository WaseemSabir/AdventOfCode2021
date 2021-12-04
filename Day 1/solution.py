with open("input.txt","r") as input:
    data = list(map(int,filter(lambda x: len(x),input.read().split("\n"))))

## part 1
part_1 = [num1 for num1, num2 in zip(data,data[1:]) if num2> num1]
print(len(part_1))

## Part 2
part_2 = [num2+num3+num4 for num1, num2, num3, num4 in zip(data,data[1:],data[2:],data[3:]) if num2+num3+num4 > num1+num2+num3]
print(len(part_2))