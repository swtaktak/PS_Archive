# 같을 수는 없다.
import sys
input = sys.stdin.readline

# a < b  inner 기준
def forward(a, b):
    if b - a <= 21:
        print('Inner circle line')
    else:
        print('Outer circle line')
def backward(a, b):
    if a - b <= 21:
        print('Outer circle line')
    else:
        print('Inner circle line')
Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    if a < b:
        forward(a, b)
    else:
        backward(a, b)