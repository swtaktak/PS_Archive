import sys
input = sys.stdin.readline

M, N = map(int, input().split())
prime_list = [True for _ in range(N + 1)]

prime_list[0] = False
prime_list[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if prime_list[i]:
        for j in range(i*i, N+1, i):
            prime_list[j] = False

for i in range(M, N+1):
    if prime_list[i]:
        print(i)