# +180, +180 +(1080 + K)

import sys
input = sys.stdin.readline
days, delay = map(int, input().split())
answer = []
cur_time = 0
for i in range(0, days * 3 + 4):
    if i == 0:
        cur_time = 900
    elif i == 1:
        cur_time = 1080
    elif i == 2:
        cur_time = 1260
    elif i % 3 == 0:
        cur_time += (delay + 1080)
    elif i % 3 != 0:
        cur_time += 180
    if cur_time >= (days) * 1440 and cur_time < (days + 1) * 1440:
        answer.append(cur_time % 1440)

print(len(answer))
for a in answer:
    ah = str(a // 60)
    am = str(a % 60)
    if len(ah) == 1:
        ah = '0' + ah
    if len(am) == 1:
        am = '0' + am
    print(ah + ':' + am)

