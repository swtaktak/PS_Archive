import sys
input = sys.stdin.readline

N, R = map(int, input().split())
dp = [[False for _ in range(N+1)] for _ in range(N+1)]
for _ in range(R):
    a, b = map(int, input().split())
    dp[a][b] = True
    dp[b][a] = True
    
days = 0
add_list = []
while R < N*(N-1)//2:
    days += 1
    add_pair = []
    for left in range(1, N):
        for right in range(left + 1, N+1):
            if not dp[left][right]:
                for mid in range(1, N+1):
                    if dp[left][mid] and dp[mid][right]:
                        add_pair.append([left, right])
                        break
        
    add_list.append(len(add_pair))
    R += len(add_pair)
    
    for a in add_pair:
        dp[a[0]][a[1]] = True
        dp[a[1]][a[0]] = True

print(days)
for a in add_list:
    print(a)