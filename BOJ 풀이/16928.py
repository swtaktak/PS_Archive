import sys
from collections import deque
input = sys.stdin.readline

visited = [-1 for _ in range(101)] # 1번부터 100번까지 최단 횟수 적을 거임.
ladder, snake = map(int, input().split())

ladder_snake_dict = {}
for _ in range(ladder+snake):
    start, end = map(int, input().split())
    ladder_snake_dict[start] = end
    

queue = deque()
queue.append(1)
visited[1] = 0
while queue:
    cur_pos = queue.popleft()
    for i in range(1, 7):
        # 주사위를 굴린다.
        next_pos = cur_pos + i
        # 100을 안 넘어 가게
        if next_pos <= 100:
            # 방문한 적이 없을 때에만 처리
            if visited[next_pos] == -1:
                # 우선 그 칸은 안 밟게 처리하고.
                visited[next_pos] = visited[cur_pos] + 1
                # 만일, 뱀사다리를 탈 수 있으면 탄 위치로 가서 추가하기. 그리고 거기도 방문이 최초여야함.
                if next_pos in ladder_snake_dict:
                    next_pos_move = ladder_snake_dict[next_pos]
                    if visited[next_pos_move] == -1:
                        visited[next_pos_move] = visited[cur_pos] + 1
                        queue.append(next_pos_move)
                # 뱀 사다리를 못타면 그냥 거기를 넣음.
                else:
                    queue.append(next_pos)
print(visited[100])