import sys
import heapq

input = sys.stdin.readline
days, milk, cookie = map(int, input().split())
need_milk = list(map(int, input().split()))

h = []
sum_milk = 0
cur_cookie = cookie
success_days = 0
# max_heap 형태로 담을 거임

while True:
    if success_days == days:
        break
    heapq.heappush(h, -need_milk[success_days])
    sum_milk += need_milk[success_days]
    if sum_milk > milk:
        cur_cookie -= 1
        if cur_cookie < 0:
            break
        else:
            cur_max = -heapq.heappop(h)
            sum_milk -= cur_max
    success_days += 1
print(success_days)