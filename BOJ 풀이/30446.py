import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for cur_num in range(1, 10 ** 5 + 1):
    if cur_num < 10 and cur_num <= N:
        cnt += 1
    rev_cur_num = str(cur_num)[::-1]
    if int(str(cur_num) + rev_cur_num) <= N:
        cnt += 1
    for add_num in range(0, 10):
        if int(str(cur_num) + str(add_num) + rev_cur_num) <= N:
            cnt += 1
print(cnt)