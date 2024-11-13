bird = int(input())
cur_cnt = 1
timed = 0

while bird > 0:
    if bird < cur_cnt:
        cur_cnt = 1
    bird -= cur_cnt
    cur_cnt += 1
    timed += 1
print(timed)