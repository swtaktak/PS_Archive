import sys
input = sys.stdin.readline

dp = [0 for _ in range(41)]
dp[0] = 1
dp[1] = 1
for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]
    
    
N = int(input())
V = int(input())
vip_list = [1]
if V > 0:
    for _ in range(V):
        vip_list.append(int(input()))
vip_list.append(N)

if V == 0:
    print(dp[N])
else:
    ans = 1
    for i in range(1, len(vip_list)):
        if i == 1 or i == len(vip_list) - 1:
            ans *= (dp[vip_list[i] - vip_list[i-1]])
        else:
            ans *= (dp[vip_list[i] - vip_list[i-1] - 1])
    print(ans)