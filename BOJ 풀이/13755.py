import sys
input = sys.stdin.readline

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

fail_flag = True
max_size = max(ax, ay, bx, by, cx, cy)

if ax < ay:
    ay, ax = ax, ay
if bx < by:
    by, bx = bx, by
if cx < cy:
    cy, cx = cx, cy

cur_list = [(ax, ay), (bx, by), (cx, cy)]
cur_list.sort(reverse = True)
ax = cur_list[0][0]
ay = cur_list[0][1]
bx = cur_list[1][0]
by = cur_list[1][1]
cx = cur_list[2][0]
cy = cur_list[2][1]

if ax*ay + bx*by + cx*cy == max_size ** 2:
    # 예제와 같은 형태로 자르는 경우
    if max_size in [bx+cx, bx+cy, by+cx, by+cy]:
        if ax == max_size:
            if ay + bx == max_size and max_size in [by + cx, by + cy]:
                fail_flag = False
            if ay + by == max_size and max_size in [bx + cx, bx + cy]:
                fail_flag = False
            if ay + cx == max_size and max_size in [cy + bx, cy + by]:
                fail_flag = False
            if ay + cy == max_size and max_size in [cx + bx, cx + by]:
                fail_flag = False  
        if ay == max_size:
            if ax + bx == max_size and max_size in [by + cx, by + cy]:
                fail_flag = False
            if ax + by == max_size and max_size in [bx + cx, bx + cy]:
                fail_flag = False
            if ax + cx == max_size and max_size in [cy + bx, cy + by]:
                fail_flag = False
            if ax + cy == max_size and max_size in [cx + bx, cx + by]:
                fail_flag = False
                    
    # 예제와 다른 형태로 자르는 경우, 즉 셋다 긴 변 가지고 있는 경우.
    if max_size in [ax+bx+cx, ax+bx+cy, ax+by+cx, ax+by+cy,
                    ay+bx+cx, ay+bx+cy, ay+by+cx, ay+by+cy]:
        if ax == bx == cx:
            fail_flag = False               
    
if fail_flag:
    print('0')
else:
    print('1')