import sys
input = sys.stdin.readline

f1, f2 = map(int, input().split())
s1, s2 = map(int, input().split())

seq = (f1 + f2 + s1 + s2 - 1) % 4
if seq == 0:
    print(4)
else:
    print(seq)