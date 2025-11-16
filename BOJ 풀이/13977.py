# 이항계수와 쿼리
# idea > 쿼리형 문제기 때문에, fact를 미리 계산해놔야 한다.
# 400만까지기 때문에 리스트를 미리 만들자.
# 그 이후, 페르마 소정리에 의하여 계산한다.
import sys
input = sys.stdin.readline
P = 1000000007

fact_list = [0 for _ in range(4000001)]
for i in range(0, 4000001):
    if i == 0:
        fact_list[i] = 1
    else:
        fact_list[i] = fact_list[i-1] * i % P

def fast_pow(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    else:
        half_val = fast_pow(a, b//2, c)
        if b % 2 == 0:
            return (half_val * half_val) % c
        else:
            return (half_val * half_val * (a % c)) % c

Q = int(input())

for _ in range(Q):
    N, K = map(int, input().split())
    
    ans = fact_list[N] * fast_pow(fact_list[N-K]*fact_list[K]%P, P-2, P) % P
    print(ans)