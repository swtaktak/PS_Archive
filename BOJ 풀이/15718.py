# 떡파이어 문제
# Idea> x1 + x2 + ,... + X(m-1) = N
# 이 때 xi는 모두 자연수 해이다.
# (M-1)H(N-M+1) 을 구하면된다.
# 즉, N-1 C (N-M+1)을 구하면 그만임.
# N-1 C M-2 을 구하면 그만
# Border Case에 주의. M = 1일 경우, N = 0이면, 1 / 아니면 0이다.
import sys
input = sys.stdin.readline

P1 = 97
P2 = 1031

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

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
    
def nCk(n, k, p):
    A = 1
    for i in range(n, n-k, -1):
        A = A * i % p
    B = fast_pow(fact_mod(k, p), p-2, p)
    return ((A*B)%p)

# 뤼카의 정리는 소수일 때만 사용 가능하다.
# 따라서 중국인의 나머지 정리를 사용할 예정이다.
def lucas(N, K, p):
    ans = 1

    while N > 0 or K > 0:
        cur_n = N % p
        cur_k = K % p
        
        if cur_n > 0 or cur_k > 0:
            if cur_n < cur_k:
                ans = 0
                break
            else:
                ans *= nCk(cur_n, cur_k, p)
                N = N // p
                K = K // p
        # 둘다 0이어도 통과
        else:
            N = N // p
            K = K // p
    return ans % p



T = int(input())
for _ in range(T):
    age, day = map(int, input().split())

    if day == 1:
        if age == 0:
            print(1)
        else:
            print(0)
            
    elif age == 0:
        if day == 1:
            print(1)
        else:
            print(0)
            
    else:
        # (age - 1) C (day - 2)를 구할 예정
        p1_r = lucas(age-1, day-2, P1)
        p2_r = lucas(age-1, day-2, P2)
        
        # 우리가 여기서 얻은 것은 x=p1_r (mod P1) x=p2_r(mod P2)
        # CRT를 적용해야 한다.
        # M = p1p2, M1 = p2, M2 = p1
        # M1y1 = 1 (mod P1)  M2y2 = 1(mod P2)
        # ans = p1_r * M1 * y1 + p2_r * M2 * y2
        # ans % 100007 구하면 된다.
        
        g, inv_M1, x1 = egcd(P2, P1)
        g, inv_M2, x2 = egcd(P1, P2)
        
        ans = ((p1_r * P2 * inv_M1) + (p2_r * P1 * inv_M2)) % 100007
        print(ans)