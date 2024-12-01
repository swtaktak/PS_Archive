# dp 풀이 시도
import sys
input = sys.stdin.readline

N = int(input())
scv_list = list(map(int, input().split()))
while len(scv_list) < 3:
    scv_list.append(0)
    
# 61 * 61 * 61 * 6 = 130만대로 충분히 가능 3차원 DP를 적용한다.
damage_type = [[1, 3, 9], [1, 9, 3], [3, 1, 9], [3, 9, 1], [9, 1, 3], [9, 3, 1]]
dp = [[[0] * 61 for _ in range(61)] for _ in range(61)] 
dp[scv_list[0]][scv_list[1]][scv_list[2]] = 1

for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0:
                for d in damage_type:
                    nx = max(0, i-d[0])
                    ny = max(0, j-d[1]) 
                    nz = max(0, k-d[2])
                    
                    if dp[nx][ny][nz] == 0 or dp[nx][ny][nz] > dp[i][j][k] + 1:
                        dp[nx][ny][nz] = dp[i][j][k] + 1                   
print(dp[0][0][0] - 1)