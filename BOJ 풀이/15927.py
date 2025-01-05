import sys
input = sys.stdin.readline

s = str(input().rstrip())

if s != s[::-1]:
    print(len(s))
else:
    c_type = []
    not_same_flag = False
    for c in s:
        if c not in c_type:
            c_type.append(c)
            if len(c_type) > 1:
                not_same_flag = True
                break
    if not_same_flag:
        print(len(s) - 1)
    else:
        print(-1)