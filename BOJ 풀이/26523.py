import sys
input = sys.stdin.readline

for _ in range(100):
    cnt = 0
    outlier_flag = False
    for _ in range(5000):
        cur_num = float(input())
        if cur_num < 0 or cur_num > 1:
            outlier_flag = True
            break
        else:
            if 0.25 <= cur_num <= 0.75:
                cnt += 1
    if outlier_flag:
        print('B')
    else:
        if cnt / 5000 >= 0.53:
            print('B')
        else:
            print('A')