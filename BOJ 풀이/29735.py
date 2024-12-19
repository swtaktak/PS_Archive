# 마지막거 배송 안하고 칼퇴함에 주의해야함

import sys
input = sys.stdin.readline

start, end = map(str, input().rstrip().split())
prev, lapsed = map(int, input().split())

start_h, start_m = start.split(":")
end_h, end_m = end.split(":")
start_time = 60 * int(start_h) + int(start_m)
end_time = 60 * int(end_h) + int(end_m)

# 하루에 몇개의 일을 처리하는가.
if (end_time - start_time) % lapsed == 0:
    day_work = (end_time - start_time) // lapsed - 1
else:
    day_work = (end_time - start_time) // lapsed

# 브실이는 언제, 몇 번째로 받는가? 맨 앞을 0으로 두면 아무런 문제가 없다.
bs_day = prev // (day_work)
bs_turn = prev % (day_work) + 1
bs_time = start_time + bs_turn * lapsed
bs_h, bs_m = bs_time // 60, bs_time % 60

if len(str(bs_h)) == 1:
    bs_h = '0' + str(bs_h)
else:
    bs_h = str(bs_h)

if len(str(bs_m)) == 1:
    bs_m = '0' + str(bs_m)
else:
    bs_m = str(bs_m)

print(bs_day)
print(bs_h + ':' + bs_m)