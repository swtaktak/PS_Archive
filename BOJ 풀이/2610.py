# 플로이드-와샬 + 유니온파인드
# 유니온 파인드로, 그룹을 구한 뒤, 플로이드-와샬로 거리합 최소를 구한다.
import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

INF = 10 ** 9 + 7 # 9ㅜㄷ이 그 숫자로
vertex = int(input())
edge = int(input())
graph = [[INF for _ in range(vertex + 1)] for _ in range(vertex + 1)]
parent = [i for i in range(vertex + 1)]

# step 1. 그래프 초기화 및 기본 입력/ 유니온 파인드로 그룹 묶기 실시
for i in range(1, vertex + 1):
    graph[i][i] = 0
        
for _ in range(edge):
    left, right = map(int, input().split())
    graph[left][right] = 1
    graph[right][left] = 1
    # 그러면서 union-find를 실시
    union(left, right)
    
# step 2. 플로이드-와샬로 거리 데이터 준비
for mid in range(1, vertex + 1):
    for left in range(1, vertex + 1):
        for right in range(1, vertex + 1):
            graph[left][right] = min(graph[left][right], graph[left][mid] + graph[mid][right])

# step 3. Union-find에서 그룹별로 묶기
group_dict = {}
group_cnt = 0
for cur_v in range(1, vertex + 1):
    cur_parent = find(cur_v)
    if cur_parent not in group_dict:
        group_cnt += 1
        group_dict[cur_parent] = [cur_v]
    else:
        group_dict[cur_parent].append(cur_v)

# step 4. 각 그룹별로 최단 거리 구하기
print(group_cnt)
cand_list = []
for cur_group in group_dict:
    cur_cands = group_dict[cur_group]
    min_dist = INF
    min_cand = INF
    
    for c in cur_cands:
        cur_dist = -1
        for o in cur_cands:
            cur_dist = max(cur_dist, graph[c][o])
        if min_dist > cur_dist:
            min_dist = cur_dist
            min_cand = c
    cand_list.append(min_cand)
    
cand_list.sort()
for c in cand_list:
    print(c)