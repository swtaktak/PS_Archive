N = int(input())
success_case = 0
cur_num = 666
while success_case < N:
    if '666' in str(cur_num):
        success_case += 1
        if success_case == N:
            break
    cur_num += 1
print(cur_num)