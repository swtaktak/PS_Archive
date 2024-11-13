import sys
import heapq
input = sys.stdin.readline

num_order = int(input())
plus_list = []
minus_list = []
heapq.heapify(plus_list)
heapq.heapify(minus_list)

for _ in range(num_order):
    cur_num = int(input())
    if cur_num == 0:
        if len(plus_list) + len(minus_list) == 0:
            print(0)
        elif len(plus_list) == 0:
            print(-minus_list[0])
            heapq.heappop(minus_list)
        elif len(minus_list) == 0:
            print(plus_list[0])
            heapq.heappop(plus_list)
        else:
            plus_abs = plus_list[0]
            minus_abs = minus_list[0]
            if plus_abs < minus_abs:
                print(plus_list[0])
                heapq.heappop(plus_list)
            elif plus_abs > minus_abs:
                print(-minus_list[0])
                heapq.heappop(minus_list)
            elif plus_abs == minus_abs:
                print(-minus_list[0])
                heapq.heappop(minus_list)
    else:
        if cur_num > 0:
            heapq.heappush(plus_list, cur_num)
        else:
            heapq.heappush(minus_list, -cur_num)