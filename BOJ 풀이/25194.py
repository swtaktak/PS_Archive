import sys
input = sys.stdin.readline

days = int(input())
works = list(map(int, input().split()))

dp = [0] * 7
dp[0] = 1

for w in works:
    temp = [0] * 7
    for j in range(7):
        if dp[j] == 1:
            temp[(w + j) % 7] = 1
            temp[j] = 1
    dp = temp.copy()
if dp[4] == 1:
    print('YES')
else:
    print('NO')