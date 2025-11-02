import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
elif N % 2 == 0 or N % 5 == 0 :
    print(-1)
else:
    cnt = 0
    cur_val = 0
    while True:
        cnt += 1
        cur_val = cur_val * 10 + 1
        if cur_val % N == 0:
            print(cnt)
            break
        else:
            cur_val = cur_val % N