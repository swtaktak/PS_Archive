# 확장 유클리드 알고리즘
# GCD가 1인 경우 해를 구할 수 있음
# candy, kid 순서로 해를 구하자.
# EGCD 알고리즘에 의해 gcd = candy * x + kid * y 해 구하게 됨.

def egcd(a, b):
    # 거꾸로 거슬러 올라가, 검산식을 대입해가는 느낌으로 맨 위까지.
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


T = int(input())
for _ in range(T):
    kid, candy = map(int, input().split())
    gcd, candy_div, kid_div = egcd(candy, kid)
    
    if gcd > 1:
        print('IMPOSSIBLE')
    else:
        while candy_div <= 0 or candy_div * candy <= kid:
            candy_div += kid
        if candy_div > 10 ** 9:
            print('IMPOSSIBLE')
        else:
            print(candy_div)
