import sys
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    x_s = (x1-x2) ** 2
    y_s = (y1-y2) ** 2
    return (x_s + y_s) ** 0.5

def dfs(level):
    global min_len
    if level == N:
        cur_len = 0
        for i in range(1, N):
            l, r = seq_list[i-1], seq_list[i]
            x1, y1 = dot_list[l][0], dot_list[l][1]
            x2, y2 = dot_list[r][0], dot_list[r][1]
            cur_len += dist(x1, y1, x2, y2)
        l, r = seq_list[-1], seq_list[0]
        x1, y1 = dot_list[l][0], dot_list[l][1]
        x2, y2 = dot_list[r][0], dot_list[r][1]
        cur_len += dist(x1, y1, x2, y2)
        min_len = min(cur_len, min_len)
        return
    
    for i in range(0, N):
        if not visited[i]:
            visited[i] = True
            seq_list.append(i)
            dfs(level + 1)
            visited[i] = False
            seq_list.pop()
            
N = int(input())
dot_list = []
min_len = 1e18

for _ in range(N):
    cx, cy = map(int, input().split())
    dot_list.append([cx, cy])

visited = [False for _ in range(N)]
seq_list = []
dfs(0)

print(min_len)