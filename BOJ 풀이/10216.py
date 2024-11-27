import sys
input = sys.stdin.readline

def is_connected(ta, tb):
    # 원의 위치관계를 활용
    ax, ay = ta[0], ta[1]
    bx, by = tb[0], tb[1]
    cutline = ta[2] + tb[2]
    if ((ax - bx) ** 2 + (ay - by) ** 2) <= cutline ** 2:
        return True
    else:
        return False

def get_top_parent(x):
    if x != parent_list[x]:
        parent_list[x] = get_top_parent(parent_list[x])
    return parent_list[x]

def union(x, y):
    x = get_top_parent(x)
    y = get_top_parent(y)
    if x != y:
        if x > y:
            parent_list[x] = y
        else:
            parent_list[y] = x

T_case = int(input())
for _ in range(T_case):
    enemy = int(input())
    enemy_list = []
    for _ in range(enemy):
        enemy_list.append(list(map(int, input().split())))
    parent_list = [i for i in range(enemy)]
    
    for i in range(enemy):
        tower_a = enemy_list[i]
        for j in range(i+1, enemy):
            tower_b = enemy_list[j]
            if is_connected(tower_a, tower_b):
                union(i, j)
    # 고유한 루트의 개수 계산
    unique_roots = set(get_top_parent(i) for i in range(enemy))
    print(len(unique_roots))