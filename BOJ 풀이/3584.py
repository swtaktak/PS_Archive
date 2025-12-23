# LCA 1탄 비효율이어도 일단 짜자.
# 하나만 구해도 되므로

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    graph = [-1 for _ in range(N + 1)]
    
    for _ in range(N-1):
        left, right = map(int, input().split())
        # left가 right의 부모다
        # 자식 right에서 거슬러 올라가 left를 만나야 한다. 부모까지
        graph[right] = left
    
    left, right = map(int, input().split())
    
    left_visited = [False for _ in range(N + 1)]
    
    # left가 먼저 길을 밝힌다.
    while True:
        left_visited[left] = True
        if graph[left] == -1:
            break
        left = graph[left]
        
    # right가 따라 간다.
    while True:
        if left_visited[right]:
            ans = right
            break
        right = graph[right]
    
    print(ans)