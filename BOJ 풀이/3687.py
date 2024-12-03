import sys
input = sys.stdin.readline

Q = int(input())
# 사전에 먼저 문제 풀이
max_digit_cnt = {2: 1, 3: 7, 4: 4, 5: 5, 6: 9, 7: 8}
min_digit_cnt = {2: 1, 3: 7, 4: 4, 5: 2, 6: 6, 7: 8} # 6은 6 or 0으로 사용해야함에 주의 최솟값 어려움.
min_dp = [0] * 101
max_dp = [0] * 101

for i in range(2, 101):
    if i == 2:
        min_dp[i] = 1
        max_dp[i] = 1
    elif i == 3:
        min_dp[i] = 7
        max_dp[i] = 7
    else:
        prev_check = [2, 3, 4, 5, 6, 7]
        # 최솟값 관련
        min_list = []
        if i in prev_check:
            min_list.append(min_digit_cnt[i])
        for p in prev_check:
            if i-p >= 2:
                cur_prev = min_dp[i-p]
                cur_add = min_digit_cnt[p]
                cur_front = cur_prev * 10 + cur_add# prev를 앞에 붙이는 경우
                cur_back = cur_add * (10 ** len(str(cur_prev))) + cur_prev
                min_list.append(min(cur_front, cur_back))
        cur_min = list(str(min(min_list)))
        for j in range(1, len(cur_min)):
            if cur_min[j] == '6':
                cur_min[j] = '0'
        min_dp[i] = int(''.join(cur_min))

        max_list = []
        if i in prev_check:
            max_list.append(max_digit_cnt[i])
        for p in prev_check:
            if i-p >= 2:
                cur_prev = max_dp[i-p]
                cur_add = max_digit_cnt[p]
                cur_front = cur_prev * 10 + cur_add# prev를 앞에 붙이는 경우
                cur_back = cur_add * (10 ** len(str(cur_prev))) + cur_prev
                max_list.append(max(cur_front, cur_back))
        max_dp[i] = max(max_list)

for _ in range(Q):
    q = int(input())
    print("%d %d" %(min_dp[q], max_dp[q]))