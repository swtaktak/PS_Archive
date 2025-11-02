import sys
import heapq
input = sys.stdin.readline

present, kid = map(int, input().split())
present_list = list(map(int, input().split()))
kid_list = list(map(int, input().split()))

present_heap = []
for p in present_list:
    heapq.heappush(present_heap, -p)

judge = True
for k in kid_list:
    cur_p = heapq.heappop(present_heap)
    cur_p *= -1
    if cur_p >= k:
        cur_p -= k
        heapq.heappush(present_heap, -cur_p)
    else:
        judge = False
        break
if judge:
    print(1)
else:
    print(0)
    