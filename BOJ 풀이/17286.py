import sys
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    x = (x2 - x1) ** 2
    y = (y2 - y1) ** 2
    return (x + y) ** 0.5

seqs = [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1]]

min_dist = 999999

pos = []
for _ in range(4):
    x, y = map(int, input().split())
    pos.append([x, y])
    
for cur_seq in seqs:
    cur_dist = 0
    for i in range(1, 4):
        x1, y1 = pos[cur_seq[i-1]][0], pos[cur_seq[i-1]][1]
        x2, y2 = pos[cur_seq[i]][0], pos[cur_seq[i]][1]
        cur_dist += dist(x1, y1, x2, y2)
    min_dist = min(min_dist, cur_dist)
print(int(min_dist))