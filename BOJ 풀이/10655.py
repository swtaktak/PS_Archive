import sys
input = sys.stdin.readline

def m_dist(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return dx + dy


N = int(input())
dist_list = [0]
coord_list = []
max_diff = 0
for i in range(N):
    # 가장 최근의 좌표.
    rx, ry = map(int, input().split())
    coord_list.append([rx, ry])
    if i >= 1:
        lx, ly = coord_list[-2][0], coord_list[-2][1]
        dist_list.append(m_dist(lx, ly, rx, ry))
    if i >= 2:
        dist_to_dist = dist_list[-2] + dist_list[-1]
        skip_dist = m_dist(coord_list[-3][0], coord_list[-3][1], rx, ry)
        benf = dist_to_dist - skip_dist
        max_diff = max(max_diff, benf)
print(sum(dist_list) - max_diff)