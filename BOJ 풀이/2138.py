import sys
input = sys.stdin.readline
ans = 100001

N = int(input())
start = list(str(input().rstrip()))
start = [int(x) for x in start]
end = list(str(input().rstrip()))
end = [int(x) for x in end]

start_0_on = start.copy()
start_0_off = start.copy()

# case 1. start_0_on
cur_case = 1
start_0_on[0] = (1-start_0_on[0])
start_0_on[1] = (1-start_0_on[1])
for i in range(1, N): 
    if start_0_on[i-1] != end[i-1]:
        start_0_on[i-1] = (1-start_0_on[i-1])
        start_0_on[i] = (1-start_0_on[i])
        if i != N-1:
            start_0_on[i+1] = (1-start_0_on[i+1])
        cur_case += 1
if start_0_on == end:
    ans = min(ans, cur_case)

# case 2. start_0_off
cur_case = 0
for i in range(1, N):
    if start_0_off[i-1] != end[i-1]:
        start_0_off[i-1] = (1-start_0_off[i-1])
        start_0_off[i] = (1-start_0_off[i])
        if i != N-1:
            start_0_off[i+1] = (1-start_0_off[i+1])
        cur_case += 1
if start_0_off == end:
    ans = min(ans, cur_case)
    
if ans == 100001:
    print(-1)
else:
    print(ans)