import sys
input = sys.stdin.readline
P = 1000000000
N = int(input())

dp_table = [[0 for _ in range(10)] for _ in range(N)]

for i in range(N):
    if i == 0:
        for j in range(1, 10):
            dp_table[i][j] = 1
    else:
        for j in range(0, 10):
            if j == 0:
                dp_table[i][j] = dp_table[i-1][1]
            elif j == 9:
                dp_table[i][j] = dp_table[i-1][8]
            else:
                dp_table[i][j] = (dp_table[i-1][j-1] + dp_table[i-1][j+1]) % P
print(sum(dp_table[-1]) % P)