import sys
import heapq
input = sys.stdin.readline
N = int(input())
min_heap = []

for i in range(N):
    cur_row = list(map(int, input().split()))
    
    if i == 0:
        for c in cur_row:
            heapq.heappush(min_heap, c)
    else:
    
        for c in cur_row:
            heapq.heappushpop(min_heap, c)

print(min_heap[0])