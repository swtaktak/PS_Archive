import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(visited, maps, rows, cols):
    queue = deque()
    queue.append([0, 0, b_lim])
    visited[0][0][b_lim] = 1
    
    while queue:
        cx, cy, b_cnt = queue.popleft()
        if cx == rows-1 and cy == cols-1:
            return visited[cx][cy][b_cnt]
        else:
            for mv in mv_list:
                nx = cx + mv[0]
                ny = cy + mv[1]
                if 0 <= nx < rows and 0 <= ny < cols:
                    # 다음 이동할 칸이 0일 경우 벽 부순 이력을 유지해 가지고 이동한다.
                    if maps[nx][ny] == '0' and visited[nx][ny][b_cnt] == 0:
                        visited[nx][ny][b_cnt] = visited[cx][cy][b_cnt] + 1
                        queue.append([nx, ny, b_cnt])
                    # 벽을 부순 적이 없는데 벽을 보았으면 거기로 갔을 리가 없다.
                    elif b_cnt > 0 and maps[nx][ny] == '1' and visited[nx][ny][b_cnt-1] == 0:
                        # 부순 칸에 넣어야 부순 이력이 유지 가능하다. 부순 이력이 뒤바뀐다.
                        visited[nx][ny][b_cnt-1] = visited[cx][cy][b_cnt] + 1
                        queue.append([nx, ny, b_cnt-1])
                    # 다른 경우는 이동이 불가능하다.                        
    return -1
    
rows, cols, b_lim = map(int, input().split())
# 이번에는 벽을 부숴야 한다. 벽을 부순적이 있으면 더 못부수게 그걸 기억해야 한다.
# 이를 해결하기 위해 3차원 리스트를 활용해야 한다.
visited = [[[0] * (1+b_lim) for _ in range(cols)] for _ in range(rows)]
maps = []
for _ in range(rows):
    cur_row = str(input().rstrip())
    maps.append(cur_row)
# 시작점을 포함하고 맨 마지막에 1을 빼줘 버리자.
result = bfs(visited, maps, rows, cols)
print(result)