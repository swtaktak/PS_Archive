import sys
input = sys.stdin.readline

def get_cnt_fact(N, p):
    cnt = 0
    cur_p = p
    while N >= cur_p:
        cnt += N // cur_p
        cur_p *= p
    return cnt

MAX = int(1000000000 ** 0.5)
prime_check = [True for _ in range(MAX + 1)]
for i in range(2, int(MAX ** 0.5 + 1)):
    if prime_check[i]:
        for j in range(i * i, MAX + 1,  i):
            prime_check[j] = False
prime_list = []
for i in range(2, MAX + 1):
    if prime_check[i]:
        prime_list.append(i)
        
while True: 
    try:
        N, K = map(int, input().split())
    except:
        break
    
    if N == 0:
        print(1)
    else:
        # K 를 소인수분해
        k_fact = {}
        for p in prime_list:
            if K < p:
                break
            elif K % p == 0:
                cur_cnt = 0
                while K % p == 0:
                    K = K // p
                    cur_cnt += 1
                k_fact[p] = cur_cnt
        if K > 1:
            k_fact[K] = 1
        gcd = 1
        
        for k in k_fact:
            N_fact_pow = get_cnt_fact(N, k)
            gcd *= (k ** (min(N_fact_pow, k_fact[k])))
        print(gcd)