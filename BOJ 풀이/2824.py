import sys
from collections import defaultdict
input = sys.stdin.readline


# step 1 각각을 소인수분해 해서 넣을 거다.
N = int(input())
N_divs = defaultdict(int)
N_list = list(map(int, input().split()))

for n in N_list:
    if n > 1:
        for i in range(2, int(n ** 0.5) + 2):
            if n % i == 0:
                while n % i == 0:
                    n = n // i
                    N_divs[i] += 1
        if n > 1:
            N_divs[n] += 1

M = int(input())
M_divs = defaultdict(int)
M_list = list(map(int, input().split()))

for n in M_list:
    if n > 1:
        for i in range(2, int(n ** 0.5) + 2):
            if n % i == 0:
                while n % i == 0:
                    n = n // i
                    M_divs[i] += 1
        if n > 1:
            M_divs[n] += 1

# 최종 정답
ans = 1
for cur_n in N_divs:
    if cur_n in M_divs:
        cur_ans = cur_n ** (min(N_divs[cur_n], M_divs[cur_n]))
        ans *= cur_ans


if len(str(ans)) <= 9:
    print(ans)
else:
    print(str(ans)[-9:])