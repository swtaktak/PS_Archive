import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N + 1)]

for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[-1])
# 이제 이걸 역으로 가자.
rev_list = []
rev_list.append(N)
cur_num = N
cur_cnt = dp[-1]
while cur_num > 1:
    if cur_num % 3 == 0 and dp[cur_num // 3] == cur_cnt - 1:
        rev_list.append(cur_num // 3)
        cur_num = cur_num // 3
    elif cur_num % 2 == 0 and dp[cur_num // 2] == cur_cnt - 1:
        rev_list.append(cur_num // 2)
        cur_num = cur_num // 2
    else:
        rev_list.append(cur_num - 1)
        cur_num = cur_num - 1
    cur_cnt -= 1

for r in rev_list:
    print(r, end = " ")