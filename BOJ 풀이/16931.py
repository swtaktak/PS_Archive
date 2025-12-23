import sys
input = sys.stdin.readline

row, col = map(int, input().split())

# 위, 아래는 볼 필요없고, 옆면 4개만 확인한다.
ans = 2 * row * col

cube = []
for _ in range(row):
    cube.append(list(map(int, input().split())))


for r in range(row):
    for c in range(col):
        # 상 확인
        if r == 0:
            ans += cube[r][c]
        else:
            ans += max(0, cube[r][c] - cube[r-1][c])
        
        # 좌 확인
        if c == 0:
            ans += cube[r][c]
        else:
            ans += max(0, cube[r][c] - cube[r][c-1])

        # 하 확인
        if r == row -1:
            ans += cube[r][c]
        else:
            ans += max(0, cube[r][c] - cube[r + 1][c])
        
        
        # 우 확인
        if c == col - 1:
            ans += cube[r][c]
        else:
            ans += max(0, cube[r][c] - cube[r][c + 1])
print(ans)