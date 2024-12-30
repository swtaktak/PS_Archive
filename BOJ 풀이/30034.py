import sys
input = sys.stdin.readline

N = int(input())
str_cut = list(map(str, input().rstrip().split()))
M = int(input())
num_cut = list(map(str, input().rstrip().split()))
K = int(input())
not_cut = list(map(str, input().rstrip().split()))
S = int(input())
std_str = str(input().rstrip())

sep_list = []
cur_ans = ''

for c in std_str:
    if c in str_cut or c in num_cut or c == ' ':
        if c not in not_cut:
            if len(cur_ans)>0:
                sep_list.append(cur_ans)
            cur_ans = ''
        else:
            cur_ans += c
    else:
        cur_ans += c
if len(cur_ans) > 0:
    sep_list.append(cur_ans)

for s in sep_list:
    print(s)