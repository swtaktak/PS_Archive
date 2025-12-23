# 2631
# 인원수 - LIS가 정답임 아 ㅋㅋㅋㅋ

N = int(input())
num_list = []

for i in range(N):
    num_list.append(int(input()))
    
dp = [1 for _ in range(N)]

for cur in range(N):
    for prev in range(cur):
        if num_list[cur] > num_list[prev]:
            dp[cur] = max(dp[cur], dp[prev] + 1)
print(N - max(dp))