# 배워봅시다 : 외판원 순환 문제 - BFS로 풀기

import sys
input = sys.stdin.readline
# 한붓그리기 하고, 맨 마지막에 돌아와야함.
# 한 번 들린 곳은 들어갈 수 없음

N = int(input())
graph = []
dp = [[0 for _ in range(1 << n) for _ in range(N)]]
for _ in range(N):
    cur_row = map(int, input().split())
    graph.append(cur_row)

