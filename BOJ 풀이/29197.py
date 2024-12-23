import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

hard_list = set()
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    if x == 0:
        cx, cy = 0, y // abs(y)
        if (cx, cy) not in hard_list:
            hard_list.add((cx, cy))
    elif y == 0:
        cx, cy = x // abs(x), 0
        if (cx, cy) not in hard_list:
            hard_list.add((cx, cy))
    else:
        d = gcd(abs(x), abs(y))
        cx, cy = x // d, y // d
        if (cx, cy) not in hard_list:
            hard_list.add((cx, cy))
print(len(hard_list))