import sys
input = sys.stdin.readline

N = int(input())
prime_list = [True] * 100001
prime_list[0] = False
prime_list[1] = False
for i in range(2, int(100001 ** 0.5) + 1):
    if prime_list[i]:
        for j in range(2*i, 100001, i):
            prime_list[j] = False
sqrt_int = max(0, int(N**0.5) - 1)
while sqrt_int ** 2 < N:
    sqrt_int += 1
if sqrt_int ** 2 == N:
    print(1)
else:
    success_flag = True
    for cur_d in range(3, N + 1, 4):
        if prime_list[cur_d] and cur_d % 4 == 3 and N % cur_d == 0:
            new_N = N
            div_cnt = 0
            while new_N % cur_d == 0:
                new_N = new_N // cur_d
                div_cnt += 1
            if div_cnt % 2 == 1:
                success_flag = False
                break
    if success_flag:
        print(2)
    else:
        while N % 4 == 0:
            N = N // 4
        if N % 8 == 7:
            print(4)
        else:
            print(3)