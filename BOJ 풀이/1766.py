import sys
import heapq

input = sys.stdin.readline
N, seq = map(int, input().split())
next_list = [[] for _ in range(N + 1)]
indegree_list = [0] * (N+1)

for _ in range(seq):
    start, end = map(int, input().split())
    indegree_list[end] += 1
    next_list[start].append(end)
    
left_list = []
heapq.heapify(left_list)
for i in range(1, N+1):
    if indegree_list[i] == 0:
        heapq.heappush(left_list, i)
answer = []
while left_list:
    cur_q = heapq.heappop(left_list)
    answer.append(cur_q)
    next_q_list = sorted(next_list[cur_q])
    for n in next_q_list:
        indegree_list[n] -= 1
        if indegree_list[n] == 0:
            heapq.heappush(left_list, n)
for i in range(N):
    if i < N-1:
        print(answer[i], end = " ")
    else:
        print(answer[i])