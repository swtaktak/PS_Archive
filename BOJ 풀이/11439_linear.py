import sys
input = sys.stdin.readline

# 선형체 버전으로 개량
N, K, M = map(int, input().split())

sieve = [0] * (N+1)
p_list = []

for i in range(2, N+1):
    if sieve[i] == 0:
        p_list.append(i)
        sieve[i] = 1
    
    for p in p_list:
        if i * p > N:
            break
        
        sieve[i * p] = 1
        if i % p == 0:
            break

ans = 1
for p in p_list:
    cur_num = p
    cur_cnt = 0
    while cur_num <= N:
        cur_cnt += (N // cur_num) - (K // cur_num) - ((N-K) // cur_num)
        cur_num *= p
    if cur_cnt > 0:
        ans = (ans * pow(p, cur_cnt, M)) % M
print(ans)