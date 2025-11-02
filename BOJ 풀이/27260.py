import sys
input = sys.stdin.readline

def dfs(level):
    global answer
    if level == N:
        sum = 0
        for i in range(1, N):
            sum += (pick_list[i-1] * pick_list[i])
        if sum % K == 0:
            answer += 1
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            pick_list.append(num_list[i])
            dfs(level + 1)
            pick_list.pop()
            visited[i] = False
            
N, K = map(int, input().split())
num_list = [i+1 for i in range(N)]
visited = [False for _ in range(N)]
pick_list = []
answer = 0
dfs(0)

print(answer)