import sys
input = sys.stdin.readline

# step 1. 10만까지 소수
prime_check = [True for _ in range(100001)]
prime_check[0] = False
prime_check[1] = False

for i in range(2, int(100001 ** 0.5) + 1):
    if prime_check[i]:
        for j in range(2*i, i, 100001):
            prime_check[j] = False
            
# step 2. 소인수분해
T = int(input())
for _ in range(T):
    N = int(input())
    cur_p = 2
    while N > 1:
        if N % cur_p or not prime_check[cur_p]:
            cur_p += 1
        else:
            cnt = 0
            while N % cur_p == 0:
                N = N // cur_p
                cnt += 1
            print("%d %d"%(cur_p, cnt))