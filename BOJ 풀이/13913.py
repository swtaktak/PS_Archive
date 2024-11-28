import sys
from collections import deque
input = sys.stdin.readline

visited = [False] * 100001
subin, brother = map(int, input().split())
visited[subin] = True

if subin > brother:
    print(subin - brother)
    for i in range(subin, brother - 1, -1):
        print(i, end = " ")
        
else: 
    queue = deque()
    queue.append([subin, [subin]])
    while queue:
        cur_pos, cur_hist = queue.popleft()
        if cur_pos == brother:
            answer = cur_hist
            break
        else:
            for next_pos in [cur_pos * 2, cur_pos + 1, cur_pos - 1]:
                if 0 <= next_pos <= 100000:
                    if not visited[next_pos]:
                        next_hist = cur_hist.copy()
                        visited[next_pos] = True
                        next_hist.append(next_pos)
                        queue.append([next_pos, next_hist])
    print(len(answer) - 1)
    for h in answer:
        print(h, end = " ")