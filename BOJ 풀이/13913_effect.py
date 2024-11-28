import sys
from collections import deque
input = sys.stdin.readline

dist = [0] * 100001
parent = [0] * 100001
subin, brother = map(int, input().split())
dist[subin] = 0

# 원래 풀이는 그냥 단순하게, 길을 직접 기억하는 풀이였다면
# 조금 더 현명하게 풀어보자. 트리 구조니까, 부모를 저장해준다.

def follow_path(cur_pos):
    hist = []
    for _ in range(dist[cur_pos] + 1):
        hist.append(cur_pos)
        cur_pos = parent[cur_pos]
    print(' '.join(map(str, hist[::-1])))

if subin > brother:
    print(subin - brother)
    for i in range(subin, brother - 1, -1):
        print(i, end = " ")

else:
    queue = deque()
    queue.append(subin)

    while queue:
        cur_pos = queue.popleft()
        if cur_pos == brother:
            print(dist[cur_pos])
            follow_path(cur_pos)
            break
        else:
            for next_pos in (cur_pos + 1, cur_pos - 1, cur_pos * 2):
                if 0 <= next_pos <= 100000 and dist[next_pos] == 0:
                    queue.append(next_pos)
                    dist[next_pos] = dist[cur_pos] + 1
                    # 부모의 위치를 기억한다!
                    parent[next_pos] = cur_pos