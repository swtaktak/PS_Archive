import sys
import math
input = sys.stdin.readline

N = int(input())
ans = str(math.factorial(N))
for c in ans[::-1]:
    if c != '0':
        print(c)
        break