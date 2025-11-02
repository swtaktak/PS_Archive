import sys
input = sys.stdin.readline

dp = [[] for _ in range(41)]
goal = int(input())
visited = [False for _ in range(2 * (10 ** 12) + 1)]
dp[0] = 0
if goal == 0:
    print(0)
else:
    visited[10**12] = True
    for i in range(1, 42):
        prev = dp[i-1]
        cur_step = 2 ** (i-1)
        success_flag = False
        for p in prev:
            if p + cur_step <= 10 ** 12 and not visited[p + cur_step + 10 ** 12]:
                visited[p + cur_step + 10 ** 12] = True
                dp[i].append(p + cur_step)
            if p - cur_step >= -10 ** 12 and not visited[p - cur_step + 10 ** 12]:
                visited[p - cur_step + 10 ** 12] = True
                dp[i].append(p + cur_step)
            if p + cur_step == goal or p - cur_step == goal:
                success_flag = True
                break
        if success_flag:
            answer = i
            break
    print(answer)          