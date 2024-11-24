import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur_std, cur_result):
    visited[cur_std] = True
    cur_cycle.append(cur_std)
    next_std = std_list[cur_std]
    
    if visited[next_std]:
        if next_std in cur_cycle:
            # 사이클이 돌고 있다. 다음 학생의 위치를 찾아 리스트를 자른다.
            cur_result += cur_cycle[cur_cycle.index(next_std):]
    else:
        dfs(next_std, cur_result)        
          
t = int(input())
for _ in range(t):
    answer = 0
    std = int(input())
    std_list = [0] + list(map(int, input().split()))
    visited = [False] * (std + 1)
    cur_result = []
    for i in range(1, std+1):
        if not visited[i]:
            cur_cycle = []
            dfs(i, cur_result)        
    print(std - len(cur_result))