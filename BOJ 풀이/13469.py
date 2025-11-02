import sys
input = sys.stdin.readline

P = 10 ** 9 + 1
square_P = int(P ** 0.5) + 1
prime_check = [True for _ in range(square_P + 1)]
prime_check[0] = False
prime_check[1] = False

for i in range(2, square_P + 1):
    if prime_check[i]:
        for j in range(2*i, i, square_P + 1):
            prime_check[j] = False
            
Q = int(input())
if Q == 1:
    print('no')
else:
    answer = True
    for i in range(2, square_P + 1):
        if Q % i == 0:
            while Q % i == 0:
                Q = Q // i
            if Q == 1:
                break
            else:
                answer = False
                break
    if answer:
        print('yes')
    else:
        print('no')