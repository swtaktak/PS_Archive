import sys
input = sys.stdin.readline

P = 1000000
N = int(input())

# dp[day][late][absent]
# 지각은 두번 하면 바로 끝
# 결석은 3콤보만 안하면 됨.
# 이전 대비해서 O(출석) L(지각) A(결석) 붙일 수 있는가. 
dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(N)]

dp[0][0][0] = 1
dp[0][1][0] = 1
dp[0][0][1] = 1

for i in range(1, N):
    # O를 붙이는 경우
    # 결석 콤보는 끊긴다.
    # 지각은 이어가기에, 지각은 분리한다.
    dp[i][0][0] += (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]) % P
    dp[i][1][0] += (dp[i-1][1][0] + dp[i-1][1][1] + dp[i-1][1][2]) % P
    
    # L을 붙이는 경우
    # 결석 콤보는 끊긴다.
    # 지각 두 번은 안된다. 맨 처음 한 번에서 가져온다.
    dp[i][1][0] += (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]) % P
    
    # A를 붙이는 경우
    dp[i][0][1] += dp[i-1][0][0]
    dp[i][0][2] += dp[i-1][0][1]
    dp[i][1][1] += dp[i-1][1][0]
    dp[i][1][2] += dp[i-1][1][1]

ans = 0
for i in range(2):
    for j in range(3):
        ans += dp[-1][i][j]
        ans = ans % P
print(ans)