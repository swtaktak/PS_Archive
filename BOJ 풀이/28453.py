import sys
input = sys.stdin.readline

def level_seg(lv):
    if lv == 300:
        return 1
    elif lv >= 275:
        return 2
    elif lv >= 250:
        return 3
    else:
        return 4


levels = int(input())
lv_list = list(map(int, input().split()))
for l in lv_list:
    print(level_seg(l), end = " ")