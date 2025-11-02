import sys
input = sys.stdin.readline

dp = [[0 for _ in range(31)] for _ in range(31)]

for i in range(31):
    if i == 0:
        dp[i][i] = 1
    else:
        for j in range(0, i+1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
# 경우의 수 계산
row, col, dels = map(int, input().split())
if dels == 0 or dels == row * col:
    answer = dp[row + col - 2][row - 1]
else:
    del_x = (dels - 1) // col + 1
    del_y = (dels - 1) % col + 1
    first_r = del_x
    first_c = del_y
    second_r = row - del_x
    second_c = col - del_y
    
    first_ans = dp[first_r + first_c - 2][first_r - 1]
    second_ans = dp[second_r + second_c][second_r]
    answer = first_ans * second_ans
print(answer)