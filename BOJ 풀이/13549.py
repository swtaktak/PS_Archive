from collections import deque
queue = deque()
subin, bro = map(int, input().split())

visited_pos = [200000] * 100001
queue.append((subin, 0))
visited_pos[subin] = True
while queue:
    cur_subin, cur_time = queue.popleft()
    if cur_subin == bro:
        if cur_time <= visited_pos[bro]:
            visited_pos[bro] = cur_time
    else:
        for new_subin in (cur_subin+1, cur_subin-1):
            if 0 <= new_subin <= 10 ** 5:
                if visited_pos[new_subin] > cur_time + 1:
                    visited_pos[new_subin] = cur_time + 1
                    queue.append((new_subin, cur_time + 1))
        if 0 <= cur_subin * 2 <= 10 ** 5:
            double_subin = cur_subin * 2
            if visited_pos[double_subin] > cur_time:
                visited_pos[double_subin] = cur_time
                queue.append((double_subin, cur_time))
print(visited_pos[bro])