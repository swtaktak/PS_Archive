import sys
input = sys.stdin.readline

num_list = [25, 30, 25, 45, 70, 95, 60, 80, 100]

dp = [1] * len(num_list)

for cur in range(0, len(num_list)):
    for prev in range(0, cur):
        if num_list[cur] > num_list[prev]:
            dp[cur] = max(dp[cur], dp[prev] + 1)
print(max(dp))