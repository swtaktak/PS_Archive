import sys
input = sys.stdin.readline

# 주의 N >= 2 기준이다.

MAX = 10 ** 7
prime_judge = [True for _ in range(MAX + 1)]
for i in range(2, int(MAX ** 0.5) + 1):
    if prime_judge[i]:
        for j in range(i * i, MAX + 1, i):
            prime_judge[j] = False
            

start, end = map(int, input().split())

ans = 0
for p in range(2, int(end ** 0.5) + 1):
    if prime_judge[p]:      
        cur = p ** 2
        while cur <= end:
            if cur >= start:
                ans += 1
            cur *= p
print(ans)