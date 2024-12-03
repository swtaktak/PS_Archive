import sys
input = sys.stdin.readline
N = int(input())
# 1->2 조합이 (N-1)!  / N!
# 따라서, 각 점에서 모든 거리의 합을 구하고 / N을 구한다.
# 왕복 고려.
def dist(x1, y1, x2, y2):
    answer = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
    return answer

coord = []
for _ in range(N):
    x, y = map(int, input().split())
    coord.append([x, y])

answer = 0
for i in range(N):
    for j in range(i, N):
        if i != j:
            x1, y1 = coord[i]
            x2, y2 = coord[j]
            answer += dist(x1, y1, x2, y2)
print(answer * 2 / N)