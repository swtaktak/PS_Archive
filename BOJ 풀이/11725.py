# dfs로 풀기! 루트는 무조건 1번이다.
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
vertex = [[] for i in range(N+1)]
# 트리 설계    
for i in range(0, N-1):
    a, b = map(int, input().split())
    vertex[a].append(b)
    vertex[b].append(a)

# 방문 여부 저장, 0일 경우는 방문 X, 아닐 경우 부모 노드를 저장
visited = [0] * (N+1)

def dfs(cur_v):
    for i in vertex[cur_v]:
        # cur_v에 연결된 것 중 간 적 없으면 자식이다.
        # 즉 그 i번째 노드의 부모는 cur_v이다.
        if visited[i] == 0:
            visited[i] = cur_v
            # i번째 중 간 적 없는 노드의 부모는 i이다.
            dfs(i)

# 출발은 1번부터, visited를 별도로 반환할 이유는 없음. 걍 저장하면 됨.
dfs(1)
for i in range(2, N+1):
    print(visited[i])
        