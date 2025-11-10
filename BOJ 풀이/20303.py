# 유니온 파인드 + 냅색
# 유니온 파인드로 하고, 사탕 개수를 가치, 우는 아이의 수를 무게로 정의해서 푼다.
# 최대 무게 = 공명컷. (주의사항! 이거 이상이면 바로 어른들이 와버림)
import sys
input = sys.stdin.readline
kid, rel, w_limit = map(int, input().split())

kid_can_list = [0] + list(map(int, input().split()))
parent = [0] + [i for i in range(1, kid + 1)]

# 유니온 파인드 부분
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

for _ in range(rel):
    left, right = map(int, input().split())
    union(left, right)

w_list = [[0, 0] for _ in range(kid + 1)] # 캔디 수 합, 우는 아이 수 합
# 이제 parent를 찾으면서, 한번 세보자
for i in range(1, kid + 1):
    cur_parent = find(i)
    w_list[cur_parent][0] += kid_can_list[i]
    w_list[cur_parent][1] += 1
    
item_list = []
for w in w_list:
    if w[1] > 0:
        item_list.append(w)

# 이제 이걸 가지고 냅색을 푼다.
# 무게 제한은 w_limit-1 까지다! 주의한다.!!!
ans = 0
dp = [[0 for _ in range(w_limit)] for _ in range(len(item_list) + 1)]

for i in range(1, len(item_list) + 1):
    cur_c, cur_w = item_list[i-1]
    for k in range(w_limit):
        dp[i][k] = dp[i-1][k]
        
        if k >= cur_w:
            # 이번 우는 아이 만큼, 캔디를 다시 뜯어낼때 효과적?인지, 이전이 나은지
            dp[i][k] = max(dp[i][k], dp[i-1][k-cur_w] + cur_c)
            
print(dp[len(item_list)][-1])