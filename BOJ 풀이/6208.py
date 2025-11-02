import sys
from collections import deque
input = sys.stdin.readline
length, pieces, budget = map(int, input().split())
coaster = {}
for _ in range(pieces):
    start, len, fun, money = map(int, input().split())
    if start not in coaster:
        coaster[start] = [[start+len, fun, money]]
    else:
        coaster[start].append([start+len, fun, money]) # arrive


q = deque()
q.append([0, 0, 0]) # end, fun, money
visited = [[-1 for _ in range(budget + 1)] for _ in range(length + 1)]
answer = -1
visited[0][0] = 0
while q:
    cur_end, cur_fun, cur_money = q.popleft()
    if cur_end == length:
        answer = max(answer, cur_fun)
    elif cur_end in coaster:
        cur_piece_list = coaster[cur_end]
        for next_end, next_fun, next_money in cur_piece_list:
            total_money = cur_money + next_money
            total_fun = cur_fun + next_fun
            
            if total_money <= budget and visited[next_end][total_money] <= total_fun:
                q.append([next_end, total_fun, total_money])
                visited[next_end][total_money] = total_fun
print(answer)