# 역원 구하기
# 덧셈역은 당연하다.
# 곱셈역의 경우는, gcd부터 체크한다. gcd가 1이 아니면 없음
# gcd가 1일 경우 Euler theorem을 적용한다. 

import sys
input = sys.stdin.readline

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

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
        
n, a = map(int, input().split())
if gcd(n, a) != 1:
    add_inv = n - a
    mul_inv = -1
else:
    # phi(N) 구현 필요 -> # N ** 0.5까지만 체크 필요
    # 어차피 소인수분해 할건데, 소인수만 구하면 됨
    prime_check = [True for _ in range(int(n ** 0.5) + 1)]
    for i in range(2, int(len(prime_check) ** 0.5) + 1):
        if prime_check[i]:
            for j in range(i*i, len(prime_check), i):
                prime_check[j] = False
    prime_list = []
    for i in range(2, len(prime_check)):
        if prime_check[i]:
            prime_list.append(i)
    div_prime = []
    cur_n = n
    for p in prime_list:
        if cur_n < p:
            break
        elif cur_n % p == 0:
            div_prime.append(p)
            while cur_n % p == 0:
                cur_n //= p
    if cur_n > 1:
        div_prime.append(cur_n)
        
    euler_n = n
    for d in div_prime:
        euler_n = euler_n * (d-1) // d
    
    add_inv = n - a
    mul_inv = fast_pow(a, euler_n-1, n)
    
print("%d %d" %(add_inv, mul_inv))