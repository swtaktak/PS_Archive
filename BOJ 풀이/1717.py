# 유니온 파인드 기초 문제로 복습.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

vertex, order = map(int, input().split())
parent_list = [i for i in range(vertex + 1)]

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
    
for i in range(order):
    cur_order, a, b = map(int, input().split())
    
    # union
    if cur_order == 0:
        union_parent(a, b)
    else:
        if find_top_parent(a) == find_top_parent(b):
            print('YES')
        else:
            print('NO')