import sys
input = sys.stdin.readline

N = int(input())
read_flag = True
plus_enjoy = [] # 즐거움이 늘어남.
same_max = 0
minus_enjoy = [] # 즐거움이 감소됨

for _ in range(N):
    use, gain = map(int, input().split())
    if use > gain:
        minus_enjoy.append([use, gain])
    elif use == gain:
        same_max = max([same_max, use])
    else:
        plus_enjoy.append([use, gain])

plus_enjoy.sort(key = lambda x: (x[0], -x[1]))
minus_enjoy.sort(key = lambda x: (-x[1], x[0]))

cur_enjoy = 0

for p in plus_enjoy:
    if cur_enjoy < p[0]:
        read_flag = False
        break
    else:
        cur_enjoy = cur_enjoy - p[0] + p[1]

if read_flag and cur_enjoy < same_max:
        read_flag = False

if read_flag:
    for m in minus_enjoy:
        if cur_enjoy < m[0]:
            read_flag = False
        else:
            cur_enjoy = cur_enjoy - m[0] + m[1]
            
if not read_flag:
    print(0)
else:
    print(1)