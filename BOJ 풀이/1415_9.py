import sys
input = sys.stdin.readline
p = 1000000007
N = int(input())
price_list = []

for _ in range(N):
    a, b = map(int, input().split())
    price_list.append(a * b * 96 // 60000)
lower, upper = map(int, input().split())

# 200개중 합이 저 범위로 나오는 경우를 어떻게 고른담..?
# 실제로 200가지 경우가 나오면 그건 무리고.
