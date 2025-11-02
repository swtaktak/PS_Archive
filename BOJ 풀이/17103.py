import sys
input = sys.stdin.readline

prime_list = [True] * 1000001
prime_list[0] = False
prime_list[1] = False
for i in range(2, int(1000001 ** 0.5) + 1):
    if prime_list[i]:
        for j in range(2 * i, 1000001, i):
            prime_list[j] = False

T = int(input())
for _ in range(T):
    ans = 0
    N = int(input())
    for i in range(2, N//2 + 1):
        if prime_list[i] and prime_list[N-i]:
            ans += 1
    print(ans)