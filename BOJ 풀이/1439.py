import sys
input = sys.stdin.readline

s = str(input().rstrip())
prev = '2'
one_cnt = 0
zero_cnt = 0

for c in s:
    if c != prev:
        if c == '2':
            prev = c
        elif c == '0':
            prev = '0'
            one_cnt += 1
        elif c == '1':
            prev = '1'
            zero_cnt += 1
print(min(one_cnt, zero_cnt))