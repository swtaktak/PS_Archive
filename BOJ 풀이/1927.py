import sys
import heapq
input = sys.stdin.readline

N = int(input())
num_list = []
heapq.heapify(num_list)

for i in range(0, N):
    cur_num = int(input())
    
    if cur_num == 0:
        if not num_list:
            print(0)
        else:
            elt = heapq.heappop(num_list)
            print(elt)
    else:
        heapq.heappush(num_list, cur_num)