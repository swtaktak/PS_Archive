# 14621
# Prim / Kruscal의 약간 응용
# Kruscal 버전 풀이
# 그래프 목록이 애초에 맞나, 틀리나를 판단하자.
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
        
def kruskal():
    sum_w = 0
    cur_edge = 0
    for i in range(len(edges)):
        a, b, cur_cost = edges[i][0], edges[i][1], edges[i][2]
        if find(a) != find(b):
            # 부모가 다르면 미연결이므로, 가중치 추가, 간선 추가, 부모 찾기
            sum_w += cur_cost
            cur_edge += 1
            union(a, b)
            if cur_edge == school - 1:
                break
    if cur_edge == school -1:
        return sum_w
    else:
        return -1

school, edge = map(int, input().split())
gender_list = ['nan'] + list(map(str, input().rstrip().split()))

visited = [False for _ in range(school + 1)]
edges = []

for _ in range(edge):
    left, right, dist = map(int, input().split())
    if gender_list[left] != gender_list[right]:
        edges.append([left, right, dist])

if len(edges) == 0:
    print(-1)
else:
    edges.sort(key = lambda x : x[2], reverse = False)
    parent = [x for x in range(school + 1)]

    answer = kruskal()
    print(answer)