# 레벨이 1~5일 경우는 문제 없다.
p = 1000000007
lv = int(input())
low_lv = [0, 4, 16, 64, 256, 1024]

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


if lv <= 5:
    print(low_lv[lv])
else:
    # nc0 + nc1 + nc2 + nc3 + nc4 + nc5 + nc6 을 계산해야함.
    # (n+1) + nc2 + (n+1)c4  + (n+1)c6로 줄인다.
    # 거기에 8방향 계산 곱해서  8^n ((n+1) + nC2 + (n+1)C4 + (n+1)C6) 
    A = fast_pow(8, lv, p)
    B = ((lv + 1) + nCk(lv, 2) + nCk(lv+1, 4) + nCk(lv+1, 6)) % p
    print((A * B) % p)