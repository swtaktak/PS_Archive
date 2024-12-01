import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num_list = list(map(int, input().split()))

left = 0
right = 0
num_cnt = [0] * 100001

max_len = 0
while right < n:
    # 수열 카운트, 오른쪽을 판단한다. (무사 통과가 된다 = 개수가 맞다)
    if num_cnt[num_list[right]] < k:
        num_cnt[num_list[right]] += 1
        right += 1
    else:
        num_cnt[num_list[left]] -= 1
        left += 1
    max_len = max(max_len, right-left)
print(max_len)