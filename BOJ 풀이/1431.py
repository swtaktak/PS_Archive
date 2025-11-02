import sys
input = sys.stdin.readline

N = int(input())

str_list = []

for _ in range(N):
    s = str(input().rstrip())
    cur_num = 0
    for c in s:
        if c.isdigit():
            cur_num += int(c)
    str_list.append([len(s), cur_num, s])

str_list.sort(key = lambda x: [x[0], x[1], x[2]])

for s in str_list:
    print(s[2])