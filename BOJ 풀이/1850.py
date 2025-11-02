import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

N, M = map(int, input().split())
d = gcd(N, M)
print('1' * d)