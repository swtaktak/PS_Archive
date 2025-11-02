import sys
input = sys.stdin.readline


N_a = int(input())
list_a = list(map(int, input().split()))

N_b = int(input())
list_b = list(map(int, input().split()))

ans_list = []

while True:
    cur_common = set(list_a) & set(list_b)
    if len(cur_common) == 0:
        break
    else:
        max_elt = max(cur_common)
        a_idx = list_a.index(max_elt)
        b_idx = list_b.index(max_elt)
        ans_list.append(max_elt)
        
        list_a = list_a[a_idx + 1:]
        list_b = list_b[b_idx + 1:]

if len(ans_list) == 0:
    print(0)
else:
    print(len(ans_list))
    for a in ans_list:
        print(a, end = ' ')
        