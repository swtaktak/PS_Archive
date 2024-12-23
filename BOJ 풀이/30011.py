import sys
input = sys.stdin.readline

polys = int(input())
poly_list = list(map(int, input().split()))
degree = 0

# 계속 내접시키면 된다.
degree += 180 * (poly_list[0] - 2)

if len(poly_list) >= 2:
    degree += 180 * sum(poly_list[1:])
print(degree)