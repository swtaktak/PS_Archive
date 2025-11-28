import sys
input = sys.stdin.readline
# mid가 마지막까지 돌지 않았다!

N = 100
print(100)
graph = [[0 for _ in range(100)] for _ in range(100)]
for i in range(100):
    for j in range(100):
        if i == j:
            graph[i][j] = 0
        elif i == 99 or j == 99:
            graph[i][j] = 1
        else:
            graph[i][j] = 10000

for i in range(100):
    for j in range(100):
        print(graph[i][j], end = " ")
    print("")