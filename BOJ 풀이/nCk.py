n, k = map(int, input().split())
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

print(nCk(n, k))