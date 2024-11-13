import sys
input = sys.stdin.readline
N = int(input())
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
ans = euler_phi(N)
print(ans)