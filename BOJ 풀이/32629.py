import sys
import math
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    N = int(input())
    
    one_side = int(math.ceil(N ** 0.5))
    if N > one_side * (one_side - 1):
        print(4 * one_side)
    else:
        print(4 * one_side - 2)