# 20955
# spanning tree를 만들라는  소리임
# 아무튼 사이클 구조는 모르지만, 일단 끊어진결 연결한 다음에 넘어간 개수만큼 걍 빼면 됨
# 뭘 빼야할지 모르지만 아무튼 갯수만 세면 되기 때문에 가능함
import sys
input = sys.stdin.readline
# step 1. union-find
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
        
vertex,edge = map(int, input().split())
parent = [x for x in range(vertex + 1)]
for _ in range(edge):
    left, right = map(int, input().split())
    union(left, right)

# step 2. count parent
par_list = {}
for i in range(1, vertex + 1):
    cur_parent = find(parent[i])
    if cur_parent not in par_list:
        par_list[cur_parent] = True

ans = 0
ans += (len(par_list) - 1)
edge += (len(par_list) - 1)

#  step 3. MST 만들기, 넘어가는만큼 제외
ans += (edge - (vertex - 1))
print(ans)