# 과연 본인의 직속상사가 회식 자리에 없는가?
# 직속상사의 직속상사의 직속상사........도 없어야만 한다.
# 이 상황에서, 결제가 가능한 사람은 몇명입니까!
import sys
from collections import deque
input = sys.stdin.readline

def bfs(boss):
    q = deque()
    buy_cnt = 0
    q.append(boss)
    
    while q:
        cur_emp = q.popleft()
        if is_eat[cur_emp]:
            buy_cnt += 1
        else:
            j_list = graph[cur_emp]
            for j in j_list:
                q.append(j)
    return buy_cnt

emp, eat = map(int, input().split())
is_eat = [False for _ in range(emp + 1)]

# 0번 인덱스는 비유효
boss_list = [100001] + list(map(int, input().split()))
# 이제 그래프를 만든다.
graph = [[] for _ in range(emp + 1)]
# 보스가 몇번인지 알아두는 것이 좋음
for i in range(1, emp + 1):
    if boss_list[i] == 0:
        boss = i
    cur_boss = boss_list[i]
    graph[cur_boss].append(i)

eat_list = list(map(int, input().split()))
for e in eat_list:
    is_eat[e] = True

# 역행이 불가능한 트리기때문에 visited 필요 없음음
answer = bfs(boss)
print(answer)