import sys
input = sys.stdin.readline
def euler_phi(N):
    if N == 1:
        return 1
    else:
        new_N = N
        for i in range(2, int(N ** 0.5) + 2):
            if N % i ==0:
                new_N *= (i-1)
                new_N = new_N // i
                while N % i == 0:
                    N = N // i
        if N > 1:
            new_N *= (N-1)
            new_N = new_N // N
        return new_N

def fast_pow(a, x, n):
    if x == 0:
        return 1
    elif x == 1:
        return a % n
    else:
        mid = fast_pow(a, x // 2, n)
        if x % 2 == 0:
            return (mid * mid) % n
        else:
            return (mid * mid * (a % n)) % n

N, E, C = map(int, input().split())
phi_N = euler_phi(N)
# 목표 E*D = 1 mod phi(N)
# gcd(E, phi(N)) = 1임이 보장
E_pow = euler_phi(phi_N) - 1

D = fast_pow(E, E_pow, phi_N)
M = fast_pow(C, D, N)
print(M)