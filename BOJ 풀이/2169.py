import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
mars = []
for _ in range(rows):
    cur_row = list(map(int, input().split()))
    mars.append(cur_row)

dp = [[0 for _ in range(cols)] for _ in range(rows)]
for r in range(rows):
    if r == 0:
        for c in range(cols):
            if c == 0:
                dp[r][c] = mars[0][0]
            else:
                dp[r][c] += dp[r][c-1] + mars[r][c]
    # 두 번째 열은, 좌방향, 우방향을 고려해야 한다. 
    else:
        left_way = [0 for _ in range(cols)]
        right_way = [0 for _ in range(cols)]
        
        # 좌뱡향 만들기. 하좌 vs 좌하 유지해가며 최댓값만 선택택
        for cur_c in range(cols):
            if cur_c == 0:
                left_way[cur_c] = dp[r-1][cur_c] + mars[r][cur_c]
            else:
                left_way[cur_c] = max(dp[r-1][cur_c], left_way[cur_c-1]) + mars[r][cur_c]
        
        # 우방향 만들기.
        for cur_c in range(cols-1, -1, -1):
            if cur_c == cols-1:
                right_way[cur_c] = dp[r-1][cur_c] + mars[r][cur_c]
            else:
                right_way[cur_c] = max(dp[r-1][cur_c], right_way[cur_c+1]) + mars[r][cur_c]
                
        for cur_c in range(cols):
            dp[r][cur_c] = max(left_way[cur_c], right_way[cur_c])

print(dp[-1][-1])