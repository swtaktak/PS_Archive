import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = [1] * N

for cur in range(0, N):
    for prev in range(0, cur):
        if num_list[cur] > num_list[prev]:
            dp[cur] = max(dp[cur], dp[prev] + 1)
print(max(dp))