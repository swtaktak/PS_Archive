N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
cur_list = []
visited = [False] * (N+1)

def print_list(num_list):
    for i in range(M):
        if i < M-1:
            print(num_list[i], end = " ")
        else:
            print(num_list[i])
            
def dfs(level, visited, cur_list):
    if len(cur_list) == M:
        print_list(cur_list)
        return
    else:
        # 동일한 깊이에서 같은 숫자를 또 안 쓰게 하기 / 해당 깊이에서 숫자가 안겹치는가.
        overlap_num = -1
        for i in range(0, N):
            if not visited[i] and overlap_num != num_list[i]:
                visited[i] = True
                cur_list.append(num_list[i])
                # 현 깊이에서, 중복 숫자 체크함. 다음 dfs에는 깊이가 달라짐.
                # dfs가 끝나면 현 깊이로 돌아오므로 중복 체크가 발생.
                overlap_num = num_list[i] 
                dfs(level+1, visited, cur_list)
                visited[i] = False
                cur_list.pop()
dfs(0, visited, cur_list)

