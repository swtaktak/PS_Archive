import sys
import math
input = sys.stdin.readline

T = int(input())
for t_case in range(1, T+1):
    N = int(input())
    answer = 0
    for n in range(int(math.log2(N)), 1, -1):
        b = int(N ** (1 / n))
        if (b ** (n + 1) - 1) // (b - 1) == N:
            answer = b
    if answer == 0:
        answer = N -1
    print("Case #%d: %d" %(t_case, answer))