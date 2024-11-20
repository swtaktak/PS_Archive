# 수 학 문 제
import sys
input = sys.stdin.readline

p = int(1e9+7) # 이거 int 처리 안하면 피망 당함.
def powered(a, b):
    # a^b mod p 계산
    if b == 1:
        return a
    else:
        if b % 2 == 0:
            return (powered(a, b//2) ** 2) % p
        else:
            return ((powered(a, b//2) **2 ) * a) % p
        
def gcd(a, b):
    while b > 0:
        a, b  = b, a%b
    return a

dice = int(input())
result = 0
for _ in range(dice):
    N, S = map(int, input().split())
    gcd_result = gcd(N, S)
    N, S = N//gcd_result, S//gcd_result
    
    result += ((S * powered(N, p-2)) %p)
    result %= p

print(result)