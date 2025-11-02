import sys
import heapq
input = sys.stdin.readline
N = int(input())
nums = []
for _ in range(N):
    cur_row = list(map(int, input().split()))
    for c in cur_row:
        heapq.heappush(nums, -c)

count = 0
while count < N:
    count += 1
    cur_elt = heapq.heappop(nums)

print(-cur_elt)
