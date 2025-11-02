import sys
input = sys.stdin.readline

diff_dict = {}
before_list = []
before = int(input())

for _ in range(before):
    x, y = map(int, input().split())
    before_list.append((x, y))

after = int(input())
for _ in range(after):
    ax, ay = map(int, input().split())
    
    for bx, by in before_list:
        dx, dy = ax-bx, ay-by
        if (dx, dy) not in diff_dict:
            diff_dict[(dx, dy)] = 0
        diff_dict[(dx, dy)] += 1

for d in diff_dict:
    if diff_dict[d] == before:
        print("%d %d" %(d[0], d[1]))
