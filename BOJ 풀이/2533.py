import sys
input = sys.stdin.readline
# dp가 두 가지 상태일때의 트리 DP
# 이 경우, dp 값 처리를 분리하여 처리한다.
# 부모 자신이 얼리어답터면, 자식은 상관이 없다.
# 부모 자신이 얼리어답터가 아니라면, 자식은 모두 얼리어답이어야 한다.
sys.setrecursionlimit(10 ** 6)
def dfs(cur_v):
    # 초기화 과정
    # 자기 자신이 얼리어답터면 1, 아니면 0
    dp[cur_v][0] = 0
    dp[cur_v][1] = 1
    for nv in graph[cur_v]:
        if not visited[nv]:
            visited[nv] = True
            dfs(nv) # 자식 노드로 내려가기
            dp[cur_v][0] += dp[nv][1]
            dp[cur_v][1] += min(dp[nv][0], dp[nv][1])
    return


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    left, right = map(int, input().split())
    graph[left].append(right)
    graph[right].append(left)

visited = [False for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N+1)] # 얼리어답 아님, 얼리어답임
visited[1] = True
dfs(1)

print(min(dp[1][0], dp[1][1]))