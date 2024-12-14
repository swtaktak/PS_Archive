import sys
input = sys.stdin.readline

N = int(input())
p = 1000000007

def fast_pow(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    else:
        half_val = fast_pow(a, b // 2, c)
        if b % 2 == 0:
            return (half_val * half_val) % c
        else:
            return (half_val * half_val * (a%c)) % c

def fact_mod(n, p):
    if n == 1:
        return 1
    else:
        val = 1
        for i in range(2, n+1):
            val = val * i % p
        return val
    
def nCk(n, k):
    A = 1
    for i in range(n, n-k, -1):
        A = A * i % p
    B = fast_pow(fact_mod(k, p), p-2, p)
    return ((A*B)%p)


answer = 0
if N == 1:
    print(0)
else:
    for i in range(0, N):
        one_cnt = i
        five_cnt = (N-1)-i
        
        if ((one_cnt) + 5 * five_cnt + 5) % 3 == 0:
    
            answer += (nCk(N-1, i) % p)
    print(answer % p)