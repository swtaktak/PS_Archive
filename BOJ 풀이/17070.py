import sys
input = sys.stdin.readline

# 가로로 도착하냐, 세로로 도착하냐, 대각선으로 도착하냐를 나눠서 계산
N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)] # 가로, 세로, 대각선으로 나눠서 경우 계산

# 최초 파이프 세팅
dp[0][0][0] = 1
dp[0][1][0] = 1
for i in range(N):
    for j in range(N):
        # 첫 줄은 가로만 이동 가능.
        if i == 0:
            if j == 0 or j == 1:
                pass
            else:
                if maps[i][j] == 1:
                    dp[0][j][0] = 0
                else:
                    # 다시 위로 올라갈 수 없으므로, 0이면 0... 1이면 1.
                    dp[0][j][0] = dp [0][j-1][0]
        else:
            # 두번째 줄부터 처리
            # 만일 첫 번째 열일 경우, 문제가 된다.
            if j == 0:
                pass
            else:
                # 문제 이미지 대로.
                if maps[i][j] == 0:
                    dp[i][j][0] += dp[i][j-1][0]  # type 1 가로 -> 가로
                    dp[i][j][1] += dp[i-1][j][1]  # type 3 세로 -> 세로
                    dp[i][j][0] += dp[i][j-1][2]  # type 5 대각 -> 가로
                    dp[i][j][1] += dp[i-1][j][2]  # type 6 대각 -> 세로 
                # 대각선 이동 판단 칸.
                if j >= 2:
                    if maps[i][j] == 0 and maps[i][j-1] == 0 and maps[i-1][j] == 0:
                        dp[i][j][2] += dp[i-1][j-1][0] # type 2 가로 -> 대각
                        dp[i][j][2] += dp[i-1][j-1][1] # type 4 세로 -> 대각
                        dp[i][j][2] += dp[i-1][j-1][2] # type 7 대각 -> 대각
                     
print(sum(dp[-1][-1]))