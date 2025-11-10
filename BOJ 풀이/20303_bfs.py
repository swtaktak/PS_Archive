import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    cur_cand_cnt = 0
    cur_kid_cnt = 0
    visited[start] = True
    while q:
        cur_v = q.pop()
        cur_kid_cnt += 1
        cur_cand_cnt += kid_can_list[cur_v]
        nv_list = graph[cur_v]
        for nv in nv_list:
            if not visited[nv]:
                visited[nv] = True
                q.append(nv)
                
    return [cur_cand_cnt, cur_kid_cnt]
kid, rel, w_limit = map(int, input().split())

kid_can_list = [0] + list(map(int, input().split()))
graph = [[] for _ in range(kid + 1)]
for _ in range(rel):
    left, right = map(int, input().split())
    graph[left].append(right)
    graph[right].append(left)
visited = [False for _ in range(kid + 1)]

item_list = []
for cur_kid in range(1, kid + 1):
    if not visited[cur_kid]:
        cur_cand_cnt, cur_kid_cnt = bfs(cur_kid)
        item_list.append([cur_cand_cnt, cur_kid_cnt])


# 이제 이걸 가지고 냅색을 푼다.
# 무게 제한은 w_limit-1 까지다! 주의한다.!!!
ans = 0
dp = [[0 for _ in range(w_limit)] for _ in range(len(item_list) + 1)]

for i in range(1, len(item_list) + 1):
    cur_c, cur_w = item_list[i-1]
    for k in range(w_limit):
        dp[i][k] = dp[i-1][k]
        
        if k >= cur_w:
            # 이번 우는 아이 만큼, 캔디를 다시 뜯어낼때 효과적?인지, 이전이 나은지
            dp[i][k] = max(dp[i][k], dp[i-1][k-cur_w] + cur_c)
            
print(dp[len(item_list)][-1])