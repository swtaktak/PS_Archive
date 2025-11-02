import sys
input = sys.stdin.readline

start = int(input())
step = 0

cur_num = start
while True:
    step += 1
    next_num = (cur_num % 10) * 10 + ((cur_num//10 + cur_num % 10) % 10)
    if next_num == start:
        break
    else:
        cur_num = next_num
print(step)