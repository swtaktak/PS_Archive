import sys
input = sys.stdin.readline

N = int(input())
color_list = [-1 for _ in range(N + 1)]
cur_color = 0
for i in range(1, int((N+1) ** 0.5 + 1)):
    if i == 1:
        cur_color += 1
        color_list[i] = 1

    else:
        if color_list[i] == -1:
            cur_color += 1
            color_list[i] = cur_color
            
            for j in range(i * i, N + 1, i):
                if color_list[j] == -1:
                    color_list[j] = cur_color
for i in range(1, N+1):
    if color_list[i] == -1:
        cur_color += 1
        color_list[i] = cur_color

print(cur_color)
for a in color_list[1:]:
    print(a, end = " ")