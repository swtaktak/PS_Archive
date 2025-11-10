# 전부 다 막힌다.
# 소수가 아니기에 역원 계산도 불가능하다.
# 답은 정공법이다.
# 정공법으로 계산해서, 소인수분해를 실시하자.
# 즉, 각 소수별로 몇개인지 모두 계산해버리는 수밖애.
# 즉, 다시 말해 어차피 4 * 10^6 까지의 소수만 확인하면 되니까.
# 그게 몇개 있는지 세 버리면 그만이다.
# nCK 는 정수임이 보장되므로, N!에 없으면 K!이나 (N-K)!에는 없음이 보장된다.
# 즉 카운트를 센 다음에, 그게 이제 M으로 나눌때 얼마가 나온지 싹다 곱해서 M으로 나누자.
# 모듈러 곱셈은 보존이 되기 때문이다.
# N, K, N-K로 나눠서, A, B, C를 하자. 솔직히 각각 따져서 빼도 이제 그리 느리진 않다.

import sys
input = sys.stdin.readline

MAX = 4 * (10 ** 6)
# 4  * 10 ** 6 까지의 소수를 얻어와야 한다.
p_check  = [True for _ in range(MAX + 1)]
for i in range(2, int(MAX ** 0.5) + 1):
    if p_check:
        for j in range(i*i, MAX + 1, i):
            p_check[j] = False
p_list = []
for i in range(2, MAX + 1):
    if p_check[i]:
        p_list.append(i)

N, K, M = map(int, input().split())

cnt_dict = {}
# Step 1. N!에 있는거 세기
for p in p_list:
    if p > N:
        break
    else:
        cur_n = N
        while cur_n > 0:
            if p not in cnt_dict:
                cnt_dict[p] = cur_n // p
            else:
                cnt_dict[p] += (cur_n // p)
            cur_n = cur_n // p

# Step 2. K! 있는거 빼기
for c in cnt_dict:
    if c > K:
        break
    else:
        cur_k = K
        while cur_k > 0:
            cnt_dict[c] -= (cur_k // c)
            cur_k = cur_k // c
            
# Step 3. N-K! 있는거 빼기
for c in cnt_dict:
    if c > N-K:
        break
    else:
        cur_k = N-K
        while cur_k > 0:
            cnt_dict[c] -= (cur_k // c)
            cur_k = cur_k // c

ans = 1

for c in cnt_dict:
    ans *= pow(c % M, cnt_dict[c], M)
    ans = ans % M
print(ans % M)
