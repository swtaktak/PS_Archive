# N은 세로줄 M은 가로줄 수는 붙어서 주어진다.
# 1이 가는길 (0, 0)에서 (N, M) 최단 경로를 구하시오!
from collections import deque
mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]
def bfs(maze_list, visited_list, rows, cols):
    answer_list = []
    pos = [0, 0]
    visited_list[0][0] = True
    queue = deque()
    queue.append((pos, 1))
    while queue:
        cur_pos, cur_cnt = queue.popleft()
        cur_x = cur_pos[0]
        cur_y = cur_pos[1]
        
        for mv in mv_list:
            nx = cur_x + mv[0]
            ny = cur_y + mv[1]
            
            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited_list[nx][ny] and maze_list[nx][ny] == '1':
                    if nx == rows-1 and ny == cols-1:
                        answer_list.append(cur_cnt + 1)
                    else:
                        visited_list[nx][ny] = True
                        queue.append(([nx, ny], cur_cnt + 1))
    return answer_list

rows, cols = map(int, input().split())
maze_list = [[] for _ in range(rows)]
visited_list = [[False for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    maze_list[i] = str(input())
answer = bfs(maze_list, visited_list, rows, cols)
print(min(answer))