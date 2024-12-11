import sys
input = sys.stdin.readline
groups, lims = map(int, input().split())
lined = list(map(int, input().split()))

cur_lim = lims
cur_wait = 0
for i in range(groups):
    if cur_lim >= lined[i]:
        cur_lim -= lined[i]
        print(cur_wait)
    else:
        cur_lim = lims - lined[i]
        cur_wait += 1
        print(cur_wait)