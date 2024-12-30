import sys
input = sys.stdin.readline

N = int(input())
name_list = []

for _ in range(N):
    cur_name = str(input().rstrip())
    name_list.append(cur_name)
asc_name = name_list.copy()
dec_name = name_list.copy()
asc_name.sort(reverse = False)
dec_name.sort(reverse = True)

if name_list == asc_name:
    print('INCREASING')
elif name_list == dec_name:
    print('DECREASING')
else:
    print('NEITHER')