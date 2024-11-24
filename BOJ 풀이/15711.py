# 환상의 짝꿍
# idea = 짝수면 무조건 성공
# 홀수일 경우 2 + (홀수) 형태만 가능
# 따라서 s-2가 홀수입니까? 가 문제임
# 길이의 상한선은 4 * 10^12, 2 * 10^6 까지의 수를 모두 구한다.

import sys
input = sys.stdin.readline

prime_list = [True] * (2 * (10 ** 6) + 1)
prime_list[0] = False
prime_list[1] = False
for i in range(2, int(len(prime_list) ** 0.5) + 1):
    if prime_list[i]:
        for j in range(2 * i, len(prime_list), i):
            prime_list[j] = False
range_prime = []
for i in range(len(prime_list)):
    if prime_list[i]:
        range_prime.append(i)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if (a + b) <= 3:
        print('NO')
    elif (a + b) % 2 == 0:
        print('YES')
    else:
        chk_num = a+b-2
        if chk_num <= 2 * (10 ** 6):
            if prime_list[chk_num]:
                print('YES')
            else:
                print('NO')
        else:
            flag = True
            for p in range_prime:
                if chk_num % p == 0:
                    flag = False
                    break
            if flag:
                print('YES')
            else:
                print('NO')