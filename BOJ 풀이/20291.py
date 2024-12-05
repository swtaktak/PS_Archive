import sys
input = sys.stdin.readline

N = int(input())
type_dict = {}

for _ in range(N):
    cur_name, cur_type = map(str, input().rstrip().split('.'))
    if cur_type not in type_dict:
        type_dict[cur_type] = 1
    else:
        type_dict[cur_type] += 1
type_list = sorted(list(type_dict.keys()))

for t in type_list:
    print("%s %d" %(t, type_dict[t]))