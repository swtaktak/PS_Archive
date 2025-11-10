# 34671
# 아 ㅋㅋ 다익이라고 할뻔
# 꼭지점이 너무 많아서 메모리 초과. 딕트로 풀자.
import sys
input = sys.stdin.readline
INF = 10**9 + 1
vertex, edge, query = map(int, input().split())
min_dict = {}
for _ in range(edge):
    start, end, dist = map(int, input().split())
    if start > end:
        start, end = end, start
    if (start, end) not in min_dict:
        min_dict[(start, end)] = dist
    else:
        min_dict[(start, end)] = min(min_dict[(start, end)], dist)
        
for _ in range(query):
    left, right = map(int, input().split())
    if left > right:
        right, left = left, right
    if (left, right) not in min_dict:
        print(-1)
    else:
        print(min_dict[(left, right)])