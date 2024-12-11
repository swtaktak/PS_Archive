import sys
from collections import defaultdict
input = sys.stdin.readline

def get_div_cnt(n):
    N_divs = defaultdict(int)
    if n > 1:
        for i in range(2, int(n ** 0.5) + 2):
            if n % i == 0:
                while n % i == 0:
                    n = n // i
                    N_divs[i] += 1
        if n > 1:
            N_divs[n] += 1
    cnt = 1
    for cur_n in N_divs:
        cnt *= (N_divs[cur_n] + 1)
    return cnt

def bin_cnt(x):
    ans = ''
    while x > 0:
        ans += str(x % 2)
        x = x // 2
    return len(ans)

# 1승은 불가능하다.
# 2승부터 몇승까지? -> 2진법 기준으로 고려하자.

N = int(input())
answer = -1
cur_try = int(N ** 0.5) + 1
for cur_pow in range(2, bin_cnt(N)):
    while cur_try ** cur_pow > N:
        cur_try -= 1
    if cur_try == 1:
        break
    elif cur_try ** cur_pow == N:
        if get_div_cnt(cur_try) == cur_pow:
            answer = cur_try
            break
print(answer)