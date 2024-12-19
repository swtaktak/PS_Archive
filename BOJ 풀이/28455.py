import sys
input = sys.stdin.readline

def union_stat(lv):
    if lv >= 250:
        return 5
    elif lv >= 200:
        return 4
    elif lv >= 140:
        return 3
    elif lv >= 100:
        return 2
    elif lv >= 60:
        return 1
    else:
        return 0

chars = int(input())
lv_list = []
for _ in range(chars):
    lv_list.append(int(input()))

lv_list.sort(reverse = True)
union_list = lv_list[:min(42, chars)]
total_stat = 0
total_lv = 0
for cur_u in union_list:
    total_lv += cur_u
    total_stat += union_stat(cur_u)
print("%d %d" %(total_lv, total_stat))