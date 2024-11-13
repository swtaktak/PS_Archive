# Euler Theorem.
# 숫자가 몇개던 상관 없다. 서로소니까 확정된다.
# phi(M)을 계산하자.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

new_M = M
answer = M
prime_check = [True] * (1+M)
# 에라토스테네스의 체.
for i in range(2, int(M**.5) + 1):
    if prime_check[i]:
        for j in range(2*i, int(M**.5)+1, i):
            prime_check[j] = False
    if new_M % i == 0:
        answer *= ((i-1)/i)
        while new_M % i == 0:
            new_M = new_M // i
    if new_M == 1:
        break
if new_M > 1:
    answer *= ((new_M-1)/new_M)
print(int(answer))



"""
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
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
ans = euler_phi(M)
print(ans)
"""