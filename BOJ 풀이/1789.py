import sys
input = sys.stdin.readline

S = int(input())
sum = 0
cur_cnt = 1

while True:
    sum += cur_cnt
    if sum > S:
        print(cur_cnt - 1)
        break
    cur_cnt += 1