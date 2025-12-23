import sys
input = sys.stdin.readline

while True:
    start, end_step, pat = map(int, input().split())
    
    if start == 0 and end_step == 0 and pat == 0:
        break
    
    pattern = list(map(int, input().split()))
    ans = start
    cur = start
    for i in range(1, end_step):
        diff = pattern[(i-1) % pat]
        cur += diff
        ans += cur
    print(ans)