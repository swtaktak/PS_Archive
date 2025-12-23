# 11243
import sys
input = sys.stdin.readline

# L inf norm은 max와 동치

MAX = 1000000
is_prime = [True for _ in range(MAX + 1)]
is_prime[1] = False
is_prime[2] = False
for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False
prime_list = []
for i in range(3, MAX + 1):
    if is_prime[i]:
        prime_list.append(i)

T = int(input())

for _ in range(T):
    M = int(input())
    is_right = False
    for p3 in range(M-4, 1, -2):
        if is_prime[p3]:
            S = M - p3
            for i in range(3, ((S + 1) // 2 + 1), 2):
                if is_prime[i] and is_prime[S - i]:
                    is_right = True
                    break
            if is_right:
                break
    print(p3)