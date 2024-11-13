import sys
input = sys.stdin.readline

t_case = int(input())
for _ in range(t_case):
    cur_s = str(input().rstrip())
    if cur_s[-1] != '.':
        print(cur_s + '.')
    else:
        print(cur_s)