import sys
from collections import deque
input = sys.stdin.readline

# ord를 활용하자.
# A = 65~ 활용
# a = 97 - 26 => 71 빼야함

def bfs(start, end):
    visited = [False] * 52
    visited[start] = True
    q = deque()
    q.append(start)
    
    while q:
        cur_v = q.popleft()
        if cur_v == end:
            return True
        nv_list = graph[cur_v]
        for nv in nv_list:
            if not visited[nv]:
                visited[nv] = True
                q.append(nv)
    return False

graph = [[] for _ in range(52)]
N = int(input())
for _ in range(N):
    left, right = map(str, input().rstrip().split(' => '))
    if left.isupper():
        left_ord = ord(left) - 65
    else:
        left_ord = ord(left) - 71
    if right.isupper():
        right_ord = ord(right) - 65
    else:
        right_ord = ord(right) - 71
    graph[left_ord].append(right_ord)
    
answer = []
for i in range(0, 52):
    for j in range(0, 52):
        if i != j:
            result = bfs(i, j)
            if result:
                answer.append([i, j])
print(len(answer))
for a in answer:
    l, r = a[0], a[1]
    if 0 <= l < 26:
        l_char = chr(l + 65)
    else:
        l_char = chr(l + 71)
    if 0 <= r < 26:
        r_char = chr(r + 65)
    else:
        r_char = chr(r + 71)
    print("%c => %c" %(l_char, r_char))    