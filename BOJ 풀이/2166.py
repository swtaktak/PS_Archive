N = int(input())
area = 0
point_list = []
y_list = []
for i in range(0, N):
    cur_x, cur_y = map(int, input().split())
    point_list.append([cur_x, cur_y])
    y_list.append(cur_y)
# 적분 아이디어를 쓰기 위해, y축을 0위로 돌려야 한다.
# 최솟값을 모두 다 빼버리자. 평행이동을 써야 한다.
y_min = min(y_list)

for i in range(0, N):
    point_list[i][1] -= y_min

for i in range(0, N):
    if i < N-1:
        cur_x, cur_y = point_list[i]
        next_x, next_y = point_list[i+1]
    else:
        cur_x, cur_y = point_list[N-1]
        next_x, next_y = point_list[0]
        
    # 양의 방향으로 넓이를 적분한다.
    if cur_x < next_x:
        area += (1/2) * (next_x - cur_x) * (cur_y + next_y)
    # 음의 방향으로 넓이를 적분한다.
    elif cur_x > next_x:
        area -= (1/2) * (cur_x - next_x) * (cur_y + next_y)
print(abs(area))