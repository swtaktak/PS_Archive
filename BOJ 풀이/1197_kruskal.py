# Kruskal Algorithm
# 가장 적은 간선부터 순서대로 선택한다.
# 유니온 파인드를 응용하여, 부모가 같은걸 봐서, 사이클 추가를 진행한다.
# 시간복잡도 O(ElogE) # 간선이 적을 때 유리함.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_top_parent(x):
    if x != parent_list[x]:
        parent_list[x] = find_top_parent(parent_list[x])
    return parent_list[x]
    
def union_parent(a, b):
    a = find_top_parent(a)
    b = find_top_parent(b)
    # 같지 않을 때만 이를 시도해야 함
    if a > b:
        parent_list[a] = b
    else:
        parent_list[b] = a
        
def kruskal():
    sum_w = 0
    cur_edge = 0
    for i in range(edge):
        a, b, cur_cost = edges[i][0], edges[i][1], edges[i][2]
        if find_top_parent(a) != find_top_parent(b):
            sum_w += cur_cost
            cur_edge += 1
        union_parent(a, b)
        if cur_edge == vertex-1:
            break
        
    return sum_w        
        
vertex, edge = map(int, input().split())
visited = [False] * (vertex + 1)
edges = []

for _ in range(edge):
    a, b, cost = map(int, input().split())
    edges.append([a, b, cost])

edges.sort(key = lambda x: x[2], reverse = False)
parent_list = [x for x in range(vertex + 1)]
answer = kruskal()
print(answer)