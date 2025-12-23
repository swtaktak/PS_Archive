import sys
input = sys.stdin.readline
# 누적 합 + 투 포인터
# 이것이 가능한 이유는, 모든 수가 자연수이기 때문이다.
# 단조 증가가 보장되어 있다.

N, target = list(map(int, input().split()))

num_list= [0] + list(map(int, input().split()))
sum_list = [0 for _ in range(N+1)]
for i in range(1, N+1):
    sum_list[i] = sum_list[i-1] + num_list[i]
    
left = 0 
right = 1
ans = 0
while left < N+1 and right < N+1:
    cur_sum = sum_list[right] - sum_list[left]
    if cur_sum < target:
        right += 1
    else:
        if cur_sum == target:
            ans += 1
        left += 1
print(ans)