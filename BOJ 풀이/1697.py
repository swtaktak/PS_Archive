from collections import deque
queue = deque()
subin, bro = map(int, input().split())

visited_pos = [-1] * 100001
queue.append(subin)
visited_pos[subin] = 0
while queue:
    cur_subin = queue.popleft()
    if cur_subin == bro:
        print(visited_pos[cur_subin])
        break
    else:
        for new_subin in (2*cur_subin, cur_subin+1, cur_subin-1):
            if 0 <= new_subin <= 10 ** 5:
                if visited_pos[new_subin] == -1:
                    visited_pos[new_subin] = visited_pos[cur_subin] + 1
                    queue.append(new_subin)
