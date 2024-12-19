import sys
input = sys.stdin.readline

def one_cnt(x):
    cnt = 0
    while x > 0:
        if x % 2 == 1:
            cnt += 1
        x = x // 2
    return cnt

N, K = map(int, input().split())
ok_N = N
while True:
    if one_cnt(ok_N) <= K:
        break
    else:
        ok_N += 1
print(ok_N - N)