import sys
input = sys.stdin.readline

def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

gcd, lcm = map(int, input().split())

ab = lcm  // gcd

s = int(ab ** 0.5)

for cur in range(s, 0, -1):
    if ab % cur == 0:
        if get_gcd(cur, ab // cur) == 1:
            a1 = cur * gcd
            a2 = (ab // cur) * gcd
            break
if a1 > a2:
    a1, a2 = a2, a1
print("%d %d" %(a1, a2))