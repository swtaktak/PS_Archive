import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

num_list = list(map(int, input().split()))
prime_list = num_list.copy()
heapq.heapify(num_list)
visited = {}
step = 0
while step < K:
    cur_elt = heapq.heappop(num_list)
    step += 1
    if step == K:
        break
    
    # 나보다 작은 수만 넣어도 많이 효율적이게 되긴 한다...
    for n in prime_list:
        if cur_elt * n not in visited:
            visited[cur_elt * n] = True
            heapq.heappush(num_list, (cur_elt * n))

print(cur_elt)