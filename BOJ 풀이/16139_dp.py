import sys
input = sys.stdin.readline

# dp로 풀어보자.

s = str(input().rstrip())

dp = [[0 for _ in range(26)] for _ in range(len(s))]

for i in range(0, len(s)):
    cur_c = ord(s[i]) - 97
    for j in range(0, 26):
        if i == 0 and j == cur_c:
            dp[i][j] = 1
        else:
            if j == cur_c:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = dp[i-1][j]

Q = int(input())
for _ in range(Q):
    cur_c, start, end = map(str, input().rstrip().split())
    start, end = int(start), int(end)
    cur_c_ord = ord(cur_c) - 97
    if start == 0:
        print(dp[end][cur_c_ord])
    else:
        print(dp[end][cur_c_ord] - dp[start-1][cur_c_ord])