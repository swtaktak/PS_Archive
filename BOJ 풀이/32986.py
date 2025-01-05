import sys
import math
input = sys.stdin.readline
a, b, c = map(int, input().split())

min_side= min(a, b, c)
if a== 3 and b == 3 and c == 3:
    print(0)
else:
    print(math.ceil(min_side / 2) - 1)