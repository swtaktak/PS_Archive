import math
log_sum = [0] * (10**7 + 1)

for i in range(1, 10**7 + 1):
    log_sum[i] = math.log10(i) + log_sum[i-1]

T = int(input())
for _ in range(T):
    cur_num = int(input())
    if cur_num == 1:
        print(1)
    else:
        print(math.ceil(log_sum[cur_num]))