import sys
input = sys.stdin.readline
answer = [[0 for _ in range(30)] for _ in range(30)]

for i in range(30):
    for j in range(30):
        if i < 15:
            if j == 15:
                answer[i][j] = 16
        elif i == 15:
            if j < 15:
                answer[i][j] = 1
            elif j > 15:
                answer[i][j] = 256
        else:
            if j == 15:
                answer[i][j] = 3840

for i in range(30):
    for j in range(30):
        print(answer[i][j], end = " ")
    print()