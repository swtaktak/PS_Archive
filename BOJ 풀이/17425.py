import sys
input = sys.stdin.readline

# 약수의 합을 빠르게 계산하자.
MAX = 1000000
prime_judge = [True for _ in range(MAX + 1)]
for i in range(2, int(MAX ** 0.5) + 1):
    if prime_judge[i]:
        for j in range(i * i, MAX + 1, i):
            prime_judge[j] = False
prime_list = []
for i in range(2, int(MAX ** 0.5) + 1):
    if prime_judge[i]:
        prime_list.append(i)


def get_div_sum(cur_num):
    ans = 1
    for p in prime_list:
        if cur_num % p == 0:
            cnt = 0
            while cur_num % p == 0:
                cnt += 1
                cur_num = cur_num // p
            cur_part = (p ** (cnt + 1) - 1) // (p - 1)
            ans *= cur_part
    if cur_num > 1:
        ans *= (1 + cur_num)
    return ans

dp = [0 for _ in range(MAX + 1)]
dp[1] = 1

for i in range(2, MAX + 1):
    cur_sum = get_div_sum(i)
    dp[i] = dp[i-1] + cur_sum
    


T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])