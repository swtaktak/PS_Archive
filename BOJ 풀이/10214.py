import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    yonsei = 0
    korea = 0
    for _ in range(9):
        cy, ck = map(int, input().split())
        yonsei += cy
        korea += ck
    if yonsei > korea:
        print('Yonsei')
    elif yonsei < korea:
        print('Korea')
    else:
        print('Draw')