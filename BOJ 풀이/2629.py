import sys
input = sys.stdin.readline
N = int(input())
w_list = list(map(int, input().split()))
dp = [set([]) for _ in range(N)]
max_w = sum(w_list)
w_check = [False] * (max_w + 1)

for i in range(N):
    if i == 0:
        dp[i].add(w_list[0])
        w_check[w_list[0]] = True
    else:
        prev_set = dp[i-1]
        cur_w = w_list[i]
        
        w_check[cur_w] = True
        dp[i].add(cur_w)
        for p in prev_set:
            dp[i].add(p)
            
            dp[i].add(p+cur_w)
            w_check[p+cur_w] = True
            
            dp[i].add(abs(p-cur_w))
            w_check[abs(p-cur_w)] = True

print(dp)
T = int(input())
t_list = list(map(int, input().split()))
for cur_t in t_list:
    if cur_t > max_w:
        print('N', end = ' ')
    elif w_check[cur_t]:
        print('Y', end = ' ')
    else:
        print('N', end = ' ')