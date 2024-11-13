N, M = map(int, input().split())
visited = [False] * (N+1)
cur_list = []
def print_list(num_list):
    for i in range(M):
        if i < M-1:
            print(num_list[i], end = " ")
        else:
            print(num_list[i])
            
def dfs(start, level, visited, cur_list):
    if level == M:
        print_list(cur_list)
        return
    
    for i in range(start + 1, N+1):
        if not visited[i]:
            visited[i] = True
            cur_list.append(i)
            dfs(i, level + 1, visited, cur_list)
            visited[i] = False
            cur_list.remove(i)
dfs(0, 0, visited, cur_list)