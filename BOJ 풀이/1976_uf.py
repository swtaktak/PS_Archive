# 유니온 파인드로 풀기
import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x > y: # x의 부모보다 y의 부모가 상위 노드라면
        parent[x] = y # x의 부모를 y의 부모로 바꾼다. (y는 find y로 부모가 됨)
    else:
        parent[y] = x

# 부모 노드를 찾는다.
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

city = int(input())
plan = int(input())
parent = [i for i in range(city)]

for i in range(city):
    cur_city = list(map(int, input().split()))
    for j in range(city):
        if cur_city[j]:
            union(i, j)

plan_list = list(map(int, input().split()))
judge = True

for i in range(1, plan):
    left, right = plan_list[i-1]-1, plan_list[i]-1
    if parent[left] != parent[right]:
        judge = False
        break

if plan == 1:
    print('YES')
elif judge:
    print('YES')
else:
    print('NO')