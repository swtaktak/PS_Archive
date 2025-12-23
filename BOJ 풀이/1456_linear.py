import sys
input = sys.stdin.readline

# 선형체 버전으로 개량
MAX = 10**7
is_comp = [False] * (MAX + 1)
primes = []
for i in range(2, MAX + 1):
    if not is_comp[i]:
        primes.append(i)
    for p in primes:
        v = i * p
        if v > MAX:
            break
        is_comp[v] = True
        if i % p == 0:
            break

start, end = map(int, input().split())

ans = 0
for p in primes:     
    cur = p ** 2
    while cur <= end:
        if cur >= start:
            ans += 1
        cur *= p
print(ans)