import sys
input = sys.stdin.readline

row, col, K = map(int, input().split())
ans = [[0 for _ in range(col)] for _ in range(row)]

if K < row + col - 1:
    print('NO')
else:
    print('YES')
    
    for i in range(row):
        for j in range(col):
            ans[i][j] = i + j + 1
            print(ans[i][j], end = " ")
        print("")