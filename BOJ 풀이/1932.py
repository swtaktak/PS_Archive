import sys
input = sys.stdin.readline

N = int(input())
pyramid = [[0 for _ in range (N)] for _ in range(N)]

for i in range(N):
    cur_line = list(map(int, input().split()))
    if i == 0:
        pyramid[i][0] = cur_line[0]
    elif i == 1:
        pyramid[i][0] = pyramid[i-1][0] + cur_line[0]
        pyramid[i][1] = pyramid[i-1][0] + cur_line[1]
    else:
        for j in range(0, i+1):
            if j == 0:
                pyramid[i][j] = pyramid[i-1][j] + cur_line[j]
            elif j < i:
                pyramid[i][j] = max(pyramid[i-1][j-1], pyramid[i-1][j]) + cur_line[j]
            else:
                pyramid[i][j] = pyramid[i-1][j-1] + cur_line[j]
print(max(pyramid[N-1]))