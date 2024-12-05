import sys
input = sys.stdin.readline

def zero_cnt(N, b):
    cnt = 0
    while True:
        if N % b != 0:
            break
        else:
            N = N // b
            cnt += 1
    return cnt

T = int(input())
for _ in range(T):
    N = int(input())
    cur_ans = 0
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            small, large = i, N // i
            
            if small != 1:
                cur_ans += zero_cnt(N, small)
            if large != small:
                cur_ans += zero_cnt(N, large)
    print(cur_ans)