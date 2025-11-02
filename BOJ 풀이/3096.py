import sys
input = sys.stdin.readline

N, M = map(int, input().split())

town_map = [[] for _ in range(N+1)]

for i in range(M):
    start, end = map(int, input().split())
    town_map[start].append(end)

result = 0
for i in range(1,N):
    for j in range(i+1, N+1):
        a = len(set(town_map[i]) & set(town_map[j]))
        result += a * (a-1) // 2

print(result)