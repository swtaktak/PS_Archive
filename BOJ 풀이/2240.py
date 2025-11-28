import sys
input = sys.stdin.readline

timed, hp = map(int, input().split())
minus_inf = -1e9
dp = [[[minus_inf for _ in range(2)] for _ in range(hp + 1)] for _ in range(timed + 1)]
dp[0][0][0] = 0

# 현재 시점에서의 판단. -> 이전 시점에서 이동했는가. 이동안했는가.... + 먹었는가, 못먹었는가

for cur_t in range(1, timed + 1):
    cur_drop = int(input()) - 1
    
    for cur_w in range(hp  + 1):
        for cur_p in range(2):
            # 현재 위치에서 자두 먹을 수 있니?
            cur_gain = 1 if cur_p == cur_drop else 0
            
            stay = dp[cur_t - 1][cur_w][cur_p]
             
            move = minus_inf
            if cur_w > 0:
                # 체력이 남았다면
                move = dp[cur_t - 1][cur_w - 1][1 - cur_p]
            
            # 현재 위치의 최적값은?
            dp[cur_t][cur_w][cur_p] = max(stay, move) + cur_gain

ans = 0
for w in range(hp + 1):
    for p in range(2):
        ans = max(ans, dp[timed][w][p])
print(ans)