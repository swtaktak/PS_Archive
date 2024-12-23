import sys
input = sys.stdin.readline
p = 10**9 + 7
def fast_pow(a, x, p):
    if x == 0:
        return 1
    elif x == 1 :
        return a % p
    
    mid = fast_pow(a, x // 2, p)
    if x % 2 == 0:
        return (mid ** 2) % p
    else:
        return (mid ** 2) * (a % p) % p 
    
    
T = int(input())
for _ in range(T):
    n = int(input())
    if n <= 2:
        print(1)
    else:
        print(fast_pow(2, n-2, p))