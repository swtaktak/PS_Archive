import sys
input = sys.stdin.readline
t_case = int(input())
for _ in range(t_case):
    cur_name = str(input().rstrip())
    print(cur_name.lower())