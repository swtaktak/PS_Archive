import sys
input = sys.stdin.readline

def is_ok(cur_num):
    if cur_num < 100:
        return True
    elif cur_num == 1000:
        return False
    else:
        cur_num_s = str(cur_num)
        if int(cur_num_s[0]) - int(cur_num_s[1]) == int(cur_num_s[1]) - int(cur_num_s[2]):
            return True
        else:
            return False

N = int(input())
dp = [0] * (N+1)

for cur_num in range(1, N + 1):
    if is_ok(cur_num):
        dp[cur_num] = dp[cur_num - 1] + 1
    else:
        dp[cur_num] = dp[cur_num - 1]
print(dp[-1])