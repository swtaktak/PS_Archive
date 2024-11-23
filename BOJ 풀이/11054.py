import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
asc_dp = [1] * N
asc_rev_dp = [1] * N

for cur in range(0, N):
    for prev in range(0, cur):
        if num_list[cur] > num_list[prev]:
            asc_dp[cur] = max(asc_dp[cur], asc_dp[prev] + 1)
# print(asc_dp)

for cur in range(N-1, -1, -1):
    for prev in range(N-1, cur, -1):
        if num_list[cur] > num_list[prev]:
            asc_rev_dp[cur] = max(asc_rev_dp[cur], asc_rev_dp[prev] + 1)
# print(asc_rev_dp)

answer = 0
for i in range(N):
    answer = max(answer, asc_dp[i] + asc_rev_dp[i] - 1)
print(answer)