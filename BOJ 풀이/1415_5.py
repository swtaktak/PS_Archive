import sys
import math
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    a, m = map(float, input().split())
    fee = a * m * 105.6 / 60000
    print(math.floor(fee))