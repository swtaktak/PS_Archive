import sys
input = sys.stdin.readline
P = 1000000007
build, left, right = map(int, input().split())

dp = [[[0 for _ in range(build + 1)] for _ in range(build + 1)] for _ in range(build + 1)]

# 현재 상태로 올 수 있는 이전의 것들이 얼마나 있는가?
# wlog, 1~N-1은 2~N으로 해석 가능하다.
# 다시 알해, 1을 끼워넣는 것이 가장 베스트일 것.
dp[1][1][1] = 1
for cur_b in range(1, build + 1):
    for cur_l in range(1, build + 1):
        for cur_r in range(1, build + 1):
            # 왼쪽에 가장 작은게 추가되는 경우는, 그냥 이전 상태에서 나머지 층 하나 높이고 왼쪽에 설치하는 것과 동일
            # 따라서,오른쪽은 변화가 없고, 왼쪽만 개수 + 1이 되므로 이전 상태는 건물-1, 왼쪽-1, 오른쪽 유지
            dp[cur_b][cur_l][cur_r] += dp[cur_b-1][cur_l-1][cur_r]
            # 오른쪽에 가장 작은게 추가되는 경우는, 그냥 이전 상태에서 나머치 층 하나 높이고 오른쪽에 설치하는 것과 동일
            # 따라서,왼쪽은 변화가 없고, 오른쪽만 개수 + 1이 되므로 이전 상태는 건물-1, 왼쪽 유지, 오른쪽 -1
            dp[cur_b][cur_l][cur_r] += dp[cur_b-1][cur_l][cur_r-1]
            # 가운데에 들어오는 경우는, 이전 상태에서 나머지 사이에 들어 오는 것
            # 동일하게 1층 높이고 들어오면 좌우 변화는 없지만 가운데 끠어 경우가 N-2개임.
            dp[cur_b][cur_l][cur_r] += (dp[cur_b-1][cur_l][cur_r]) * (cur_b - 2)
            dp[cur_b][cur_l][cur_r] %= P

print(dp[build][left][right])