# 3마를 최대한 적게
import sys
input = sys.stdin.readline

only_3, only_4, both = map(int, input().split())
no_flag = False
# impossible_check
if only_3 % 3 != 0:
    both -= (3 - (only_3 % 3))
    only_3 += (3 - (only_3 % 3))
    if both < 0:
        no_flag = True

if not no_flag and only_4 % 4 != 0:
    both -= (4 - (only_4 % 4))
    only_4 += (4 - (only_4 % 4))
    if both < 0:
        no_flag = True

if not no_flag:
    max_4 = both // 4
    
    left_success = False
    for i in range(max_4, -1, -1):
        left = both - 4 * i
        if left % 3 == 0:
            left_success = True
            only_3 += left
            only_4 += (4 * i)
            break
    if not left_success:
        no_flag = True

if no_flag:
    print(-1)
else:
    print("%d %d" %(only_3 // 3, only_4 // 4))