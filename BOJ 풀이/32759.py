import sys
input = sys.stdin.readline
p = 10 ** 9 + 7

max_step, stone = map(int, input().split())
s_list = list(map(int, input().split()))
s_list.sort()

# case 1 > 최대치가 둘 다 음수일 경우 (0, 0) 포함해서 처리.
if s_list[-2] <= 0 and s_list[-1] <= 0:
    answer = (s_list[-2] + s_list[-1]) % p

else:
    cur_step = 0
    second = s_list[-2]
    first = s_list[-1]
    # case 2 > 하나는 음수, 하나는 양수일 경우 먼저 양수화
    if second < 0 and first > 0:
        while second <= 0:
            second = first + second
            cur_step += 1
            if cur_step == max_step:
                answer = second
                break
        if first < second:
            first, second = second, first
    # case 3 > 모두 양수일 경우
    if cur_step < max_step:
        left_step = max_step - cur_step
        # 남은 횟수 만큼 피보나치 형태
        dp = [second, first] + [0] * (left_step)
        for i in range(2, len(dp)):
            dp[i] = (dp[i-1] + dp[i-2]) % p
        answer = dp[-1]
print(answer % p)