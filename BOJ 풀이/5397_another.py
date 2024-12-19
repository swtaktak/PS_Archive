# < >, 커서 기준이 아니라 좌우로 리스트를 직접 빼서 관리하자. 헷갈린다.
# 즉, 커서의 좌측과 우측을 관리하자.

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    logs = str(input().rstrip())
    c_left = []
    c_right = []
    
    for l in logs:
        if l == ">":
            if c_right:
                c_left.append(c_right.pop())
        elif l == "<":
            if c_left:
                c_right.append(c_left.pop())
        elif l == "-":
            if c_left:
                c_left.pop()
        else:
            c_left.append(l)
    print("".join(c_left) + "".join(c_right[::-1]))