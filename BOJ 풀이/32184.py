import sys
input = sys.stdin.readline

A, B = map(int, input().split())
if A % 2 == 0:
    A = A - 1
if B % 2 == 1:
    B = B + 1
pages = B - A + 1
print(pages//2)