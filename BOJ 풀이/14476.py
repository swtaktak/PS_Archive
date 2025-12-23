# 여러 수의 gcd를 구할때는 두개씩 한다.

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

N = int(input())
num_list = list(map(int, input().split()))


left_gcd = [0 for _ in range(N)]
right_gcd = [0 for _ in range(N)]

for i in range(N):
    if i == 0:
        left_gcd[i] = num_list[i]
    else:
        left_gcd[i] = gcd(num_list[i], left_gcd[i-1])

for i in range(N-1, -1, -1):
    if i == N-1:
        right_gcd[i] = num_list[i]
    else:
        right_gcd[i] = gcd(num_list[i], right_gcd[i+1])

ans_gcd = -1
ans_num = -1
for i in range(0, N):
    if i == 0:
        cur_gcd = right_gcd[1]
        if num_list[i] % cur_gcd != 0:
            if ans_gcd < cur_gcd:
                ans_num = num_list[i]
                ans_gcd = cur_gcd
    elif i == N-1:
        cur_gcd = left_gcd[N-2]
        if num_list[i] % cur_gcd != 0:
            if ans_gcd < cur_gcd:
                ans_num = num_list[i]
                ans_gcd = cur_gcd
    else:
        cur_gcd = gcd(left_gcd[i-1], right_gcd[i+1])
        if num_list[i] % cur_gcd != 0:
            if ans_gcd < cur_gcd:
                ans_num = num_list[i]
                ans_gcd = cur_gcd
if ans_gcd > 0:
    print("%d %d" %(ans_gcd, ans_num))
else:
    print(-1)