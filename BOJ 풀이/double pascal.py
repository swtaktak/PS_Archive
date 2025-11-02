num_list = [[0 for _ in range(100)] for _ in range(101)]
for row in range(100):
    if row == 0:
        num_list[0][0] = 3
    elif row == 1:
        num_list[1][1] = 4
        num_list[1][0] = 4
    else:
        for col in range(0, row + 1):
            if col == 0 or col == row:
                num_list[row][col] = row + 3
            else:
                num_list[row][col] = num_list[row-1][col-1] + num_list[row-1][col]

for r in num_list:
    print(r)
                
# 00
# 10 11
# 20 21 22