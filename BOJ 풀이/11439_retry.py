import sys
input = sys.stdin.readline

MAX = 4 * (10 ** 6)
p_check  = [True for _ in range(MAX + 1)]
for i in range(2, int(MAX ** 0.5) + 1):
    if p_check[i]:
        for j in range(i*i, MAX + 1, i):
            p_check[j] = False
p_list = [i for i in range(2, MAX + 1) if p_check[i]]

N, K, M = map(int, input().split())

ans = 1
for p in p_list:
    if p > N:
        break
    else:
        cur_num = p
        cur_cnt = 0
        while cur_num <= N:
            cur_cnt += (N // cur_num) - (K // cur_num) - ((N-K) // cur_num)
            cur_num *= p
        if cur_cnt > 0:
            ans = (ans * pow(p, cur_cnt, M)) % M
print(ans)