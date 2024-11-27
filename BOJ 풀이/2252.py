import sys
from collections import deque
input = sys.stdin.readline

std, comp = map(int, input().split())
next_list = [[] for _ in range(std + 1)]
indegree_list = [0] * (std + 1)

for _ in range(comp):
    start, end = map(int, input().split())
    next_list[start].append(end)
    indegree_list[end] += 1

queue = deque()
for i in range(1, std+1):
    if indegree_list[i] == 0:
        queue.append(i)
        
answer = []
while queue:
    cur_std = queue.popleft()
    answer.append(cur_std)
    
    for cur_next in next_list[cur_std]:
        indegree_list[cur_next] -= 1
        if indegree_list[cur_next] == 0:
            queue.append(cur_next)
for i in range(std):
    if i < std-1:
        print(answer[i], end = " ")
    else:
        print(answer[i])