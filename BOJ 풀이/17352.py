# 유파 또 복습해야겠지?
import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x
        
        
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

N = int(input())

parent = [0] + [i for i in range(1, N+1)]

if N == 2:
    print('1 2')
else:
    for i in range(N-2):
        l, r = map(int, input().split())
        union(l, r)
    parent_list = []
    
    for i in range(1, N+1):
        cur_parent = find(i)
        if cur_parent not in parent_list:
            parent_list.append(cur_parent)
    
    print("%d %d" %(parent_list[0], parent_list[1]))