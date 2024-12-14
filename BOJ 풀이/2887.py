# 이번엔 크루스칼로 풀어보기
import sys
input = sys.stdin.readline

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
    for i in range(3 * (N-1)):
        a, b, cur_cost = edges[i][0], edges[i][1], edges[i][2]
        if find_top_parent(a) != find_top_parent(b):
            sum_w += cur_cost
            cur_edge += 1
        union_parent(a, b)
        if cur_edge == N-1:
            break
        
    return sum_w 


N = int(input())
points = []
for i in range(N):
    # 행성 번호까지 같이 지정해야 한다! 그래야 그래프 구분이 되니까.
    points.append(list(map(int, input().split())) + [i])

parent_list = [i for i in range(N)]
edges = []
# x좌표
for c in range(3):
    points.sort(key = lambda x: x[c], reverse = False)
    for i in range(1, N):
        lx, lp, rx, rp = points[i-1][c], points[i-1][3], points[i][c], points[i][3]
        edges.append([lp, rp, rx - lx])
        
edges.sort(key = lambda x: x[2], reverse = False)
answer = kruskal()
print(answer)