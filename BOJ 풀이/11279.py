import sys
import heapq
input = sys.stdin.readline

num_list = []
heapq.heapify(num_list)

num_order = int(input())

for _ in range(num_order):
    cur_num = int(input())
    if cur_num != 0:
        heapq.heappush(num_list, -cur_num)
    else:
        if len(num_list) == 0:
            print(0)
        else:
            print(-num_list[0])
            heapq.heappop(num_list)