def get_sum_gen(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

N = int(input())
cur_check = N
min_gen_num = N+1
flag = False
while cur_check > 0:
    if get_sum_gen(cur_check)+cur_check == N:
        flag = True
        if cur_check < min_gen_num:
            min_gen_num = cur_check
        cur_check -= 1
    else:
        cur_check -= 1
if not flag:
    print(0)
else:
    print(min_gen_num)