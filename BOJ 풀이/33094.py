import sys
from collections import deque

input = sys.stdin.readline
days, milk, cookie = map(int, input().split())
need_milk = list(map(int, input().split()))

max_date = 0

q = deque()
q.append([0, milk, cookie])

while q:
    cur_day, cur_milk, cur_cookie = q.popleft()
    if cur_day == days:
        max_date = days
        break
    else:
        today_need_milk = need_milk[cur_day]
        if today_need_milk <= cur_milk:
            q.append([cur_day + 1, cur_milk - today_need_milk, cur_cookie])
            max_date = max(max_date, cur_day + 1)
        if cur_cookie > 0:
            q.append([cur_day + 1, cur_milk, cur_cookie - 1])
            max_date = max(max_date, cur_day + 1)
print(max_date)