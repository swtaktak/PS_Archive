import sys
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    x_s = (x1-x2) ** 2
    y_s = (y1-y2) ** 2
    return (x_s + y_s) ** 0.5
            
N = int(input())
dot_list = []
for _ in range(N):
    cx, cy = map(int, input().split())
    dot_list.append([cx, cy])

dot_list.sort(key = lambda x: [x[1], x[0]])
start_dot = dot_list[0]
left_list = []
right_list = []
for cur_d in dot_list[1:]:
    cx, cy = cur_d[0], cur_d[1]
    if start_dot[0] > cx:
        left_list.append(cur_d)
    else:
        right_list.append(cur_d)

left_list.sort(key = lambda x: x[1])
right_list.sort(key = lambda x: -x[1])

dot_list = [start_dot] + left_list + right_list + [start_dot]
cur_len = 0

for i in range(1, N + 1):
    l, r = i-1, i
    x1, y1 = dot_list[l][0], dot_list[l][1]
    x2, y2 = dot_list[r][0], dot_list[r][1]
    cur_len += dist(x1, y1, x2, y2)
print(cur_len)