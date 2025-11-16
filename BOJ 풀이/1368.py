# 크루스칼 알고리즘 vs # 프림 알고리즘
# 문제는... 이게 물을 가져오는게 좋은지, 파는 게 좋은지 모른다.
# 그리고 하나의 수원은 필요..?
# 수원을 0번으로 해서 가상의 노드를 만든다.!
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
            sum_w += cur_cost
            cur_edge += 1
            union(a, b)
        if cur_edge == field:
            break
    return sum_w
        
field = int(input())
edges = []
for cur_field in range(1, field + 1):
    cost = int(input())
    # 수원은 0번이다.
    edges.append((0, cur_field, cost))

# 이제 1번부터 N번 밭 까지의 cost list 생성
for cur_field in range(1, field + 1):
    cur_list = [0] + list(map(int, input().split()))
    for next_field in range(1, field + 1):
        if cur_field != next_field:
            edges.append([cur_field, next_field, cur_list[next_field]])
            
# 수원인 0번을 포함하여 크루스칼.
parent = [i for i in range(field + 1)]
edges.sort(key = lambda x: x[2], reverse = False)
ans = kruskal()
print(ans)