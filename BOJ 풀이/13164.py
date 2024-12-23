import sys
import heapq
input = sys.stdin.readline
std, group = map(int, input().split())
tall_list = list(map(int, input().split()))
total_sum = 0
diff_list = []

if std == 1:
    print(0)
else:
    for i in range(1, std):
        total_sum += (tall_list[i] - tall_list[i-1])
        heapq.heappush(diff_list, tall_list[i-1] - tall_list[i])
    
    for i in range(group - 1):
        cur_diff = heapq.heappop(diff_list)
        total_sum += cur_diff
    print(total_sum)