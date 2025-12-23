import sys
input = sys.stdin.readline

N = int(input())
prev = list(map(int, input().split()))
after = list(map(int, input().split()))

if N <= 2:
    print('good puzzle')
else:
    prev_nbd_dict = {}
    for i in range(N):
        if i == 0:
            prev_nbd_dict[prev[i]] = (prev[1], prev[-1])
        elif i == N-1:
            prev_nbd_dict[prev[i]] = (prev[0], prev[i-1])
        else:
            prev_nbd_dict[prev[i]] = (prev[i-1], prev[i+1])
    after_nbd_dict = {}
    for i in range(N):
        if i == 0:
            after_nbd_dict[after[i]] = (after[1], after[-1])
        elif i == N-1:
            after_nbd_dict[after[i]] = (after[0], after[i-1])
        else:
            after_nbd_dict[after[i]] = (after[i-1], after[i+1])
    nbd_flag = True
    for i in range(1, N+1):
        prev_1 = prev_nbd_dict[i][0]
        prev_2 = prev_nbd_dict[i][1]
        if prev_1 not in after_nbd_dict[i] or prev_2 not in after_nbd_dict[i]:
            nbd_flag = False
            break
    if nbd_flag:
        print('good puzzle')
    else:
        print('bad puzzle')