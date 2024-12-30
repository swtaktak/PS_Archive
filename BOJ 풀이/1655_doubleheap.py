import sys
import heapq
input = sys.stdin.readline
# 이진탐색으로는 살짝 무리. 다른 방법을 써보자
left_heap = [] # max_heap
right_heap = [] # min_heap

N = int(input())
for _ in range(N):
    cur_num = int(input())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -cur_num)
    else:
        heapq.heappush(right_heap, cur_num)
    
    if right_heap and right_heap[0] < -left_heap[0]:
        left_val = -heapq.heappop(left_heap)
        right_val = heapq.heappop(right_heap)
        
        heapq.heappush(right_heap, left_val)
        heapq.heappush(left_heap, -right_val)
    print(-left_heap[0])