with open("input.txt") as input:
    data = list(filter(lambda x: len(x), input.read().split("\n")))

random = list(map(int, filter(lambda x: len(x), data[0].split(","))))
tables = [[list(map(lambda x: [x, False],list(map(int, filter(lambda x: len(x), line.split(" ")))))) for line in data[i:i+5]] for i in range(1, len(data), 5)]

print()
print("Part 1")

solution_found = False

for rand in random:
    if solution_found:
        break
    for table in tables:
        sum_i = 0
        row_check = False
        col_check = False

        for row_i, row in enumerate(table):
            for col_i, pair in enumerate(row):
                if pair[0]==rand:
                    pair[1] = True
                    
                    row_check = True
                    col_check = True

                    for p in table[row_i]:    
                        row_check = (row_check and p[1])

                    for index in range(len(table)):
                        col_check = (col_check and table[index][col_i][1])

                if not pair[1]:
                    sum_i += pair[0]

        found_winner = (row_check or col_check)
        if found_winner:
            print(f"Solution : {sum_i*rand}")
            solution_found = True

print()
print("Part 2")

won = [False for _ in tables]
all_won = False
solution_found = False

for rand in random:
    if solution_found:
        break
    for i_t, table in enumerate(tables):
        sum_i = 0
        row_check = False
        col_check = False
        all_won = True

        for row_i, row in enumerate(table):
            for col_i, pair in enumerate(row):
                if pair[0]==rand:
                    pair[1] = True
                    
                    row_check = True
                    col_check = True

                    for p in table[row_i]:    
                        row_check = (row_check and p[1])

                    for index in range(len(table)):
                        col_check = (col_check and table[index][col_i][1])

                if not pair[1]:
                    sum_i += pair[0]

        found_winner = (row_check or col_check)
        if found_winner:
            won[i_t] = True
            for one in won:
                all_won = (all_won and one)

            if all_won:
                print(f"Solution : {sum_i*rand}")
                solution_found = True
                break