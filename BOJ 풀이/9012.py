import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = str(input().rstrip())
    stack = []
    
    flag = True
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                flag = False
                break
            else:
                stack.pop()
    if stack:
        flag = False
    if flag:
        print('YES')
    else:
        print('NO')