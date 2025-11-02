import sys
input = sys.stdin.readline

vertex, edge = map(int, input().split())
parent_list = [i for i in range(vertex + 1)]

def find_top_parent(x):
    if x != parent_list[x]:
        parent_list[x] = find_top_parent(parent_list[x])
    return parent_list[x]

def union_parent(a, b):
    a = find_top_parent(a)
    b = find_top_parent(b)
    if a != b:
        if a > b:
            parent_list[a] = b
        else:
            parent_list[b] = a

for _ in range(edge):
    a, b = map(int, input().split())
    union_parent(a, b)

# 주의사항. union을 한다고, 그 자식이 업데이트 되지는 않아서,  자식까지 최대 부모 찾으려면 한번 돌아야 한다.
for i in range(1, vertex+1):
    parent_list[i] = find_top_parent(parent_list[i])
    
parent_list = list(set(parent_list[1:]))
print(len(parent_list) - 1)