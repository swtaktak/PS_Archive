# 배워봅시다. 뤼카의 정리
import sys
input = sys.stdin.readline

# 이항 계수 3에서 배운, 빠른 nCk 코드 사용
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


# 뤼카의 정리는 소수일 때만 사용 가능하다.
N, K, p = map(int, input().split())

ans = 1

while N > 0 or K > 0:
    cur_n = N % p
    cur_k = K % p
    
    if cur_n > 0 or cur_k > 0:
        if cur_n < cur_k:
            ans = 0
            break
        else:
            ans *= nCk(cur_n, cur_k)
            N = N // p
            K = K // p
    # 둘다 0이어도 통과
    else:
        N = N // p
        K = K // p
        
print(ans % p)