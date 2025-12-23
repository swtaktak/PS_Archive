import sys
input = sys.stdin.readline

MAX = int(1000000000 ** 0.5)
prime_judge = [True for _ in range(MAX + 1)]
for i in range(2, int(MAX ** 0.5) + 1):
    if prime_judge[i]:
        for j in range(i * i, MAX + 1, i):
            prime_judge[j] = False
prime_list = []
for i in range(2, MAX + 1):
    if prime_judge[i]:
        prime_list.append(i)
        
while True:
    N = int(input())
    if N == 0:
        break
    elif N == 1:
        print(0)
    else:
        cur = N
        ans = N
        for p in prime_list:
            if p > cur:
                break
            if cur % p == 0:
                ans = ans * (p-1) // p
            while cur % p == 0:
                cur = cur // p
        if cur > 1:
            ans = ans * (cur - 1) // cur
        print(ans)