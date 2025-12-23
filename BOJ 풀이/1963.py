import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    visited = {}
    ans = -1
    for p in prime_list:
        visited[p] = False
    q = deque()
    q.append((start, 0))
    visited[start] = True
    while q:
        cur_num, cur_step = q.popleft()
        if cur_num == end:
            ans = cur_step
            break
        for nv in prime_graph[cur_num]:
            if not visited[nv]:
                visited[nv] = True
                q.append((nv, cur_step + 1))
                
    if ans == -1:
        return 'impossible'
    else:
        return ans

def is_only_one_diff(start, end):
    s = str(start)
    e = str(end)
    if s[0] != e[0] and s[1] == e[1] and s[2] == e[2] and s[3] == e[3]:
        return True
    if s[0] == e[0] and s[1] != e[1] and s[2] == e[2] and s[3] == e[3]:
        return True
    if s[0] == e[0] and s[1] == e[1] and s[2] != e[2] and s[3] == e[3]:
        return True
    if s[0] == e[0] and s[1] == e[1] and s[2] == e[2] and s[3] != e[3]:
        return True
    return False

N = 9999
prime_check = [True for _ in range(N+1)]
for i in range(2, int(N ** 0.5) + 1):
    if prime_check[i]:
        for j in range(i*i, N+1, i):
            prime_check[j] = False
prime_list = []
for i in range(1001, N+1):
    if prime_check[i]:
        prime_list.append(i)

# graph가 필요함
prime_graph = {}
for p in prime_list:
    prime_graph[p] = []
for start in prime_list:
    for end in prime_list:
        if is_only_one_diff(start, end):
            prime_graph[start].append(end)
            
T = int(input())
for _ in range(T):
    start, end = map(int, input().split())
    result = bfs(start, end)
    print(result)