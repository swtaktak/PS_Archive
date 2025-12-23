import sys
input = sys.stdin.readline

def get_div_sum(N):
    ans = 0
    i = 2
    while i * i <= N:
        if N % i == 0:
            ans += i
            if i != N // i:
                ans += (N // i)
        i += 1
    ans += 1
    return ans

N = int(input())

while True:
    a = get_div_sum(N)
    if get_div_sum(a) == N and a != N:
        print("%d %d" %(N, a))
        break
    N += 1
