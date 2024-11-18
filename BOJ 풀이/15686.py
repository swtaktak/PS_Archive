import sys
input = sys.stdin.readline
def chick_dist(chick_list, house_list):
    global min_length
    sum_dist = 0
    for cur_h in house_list:
        cur_min_dist = sys.maxsize
        for i in range(len(chick_list)):
            if visited[i]:
                cur_dist = abs(cur_h[0] - chick_list[i][0]) + abs(cur_h[1] - chick_list[i][1])
                if cur_dist < cur_min_dist:
                    cur_min_dist = cur_dist
        sum_dist += cur_min_dist
    if sum_dist < min_length:
        min_length = sum_dist

def dfs(pick_num, cur_pos):
    global min_length
    if pick_num <= chick_cut:
        chick_dist(chick_list, house_list)
    elif pick_num > chick_cut:
        pass
    for i in range(cur_pos, len(chick_list)):
        if not visited[i]:
            visited[i] = True
            dfs(pick_num + 1, i + 1)
            visited[i] = False
    
N, chick_cut = map(int, input().split())
maps = []
house_list = []
chick_list = []

for i in range(N):
    cur_row = list(map(int, input().split()))
    for j in range(N):
        if cur_row[j] == 1:
            house_list.append([i, j])
        elif cur_row[j] == 2:
            chick_list.append([i, j])
    maps.append(cur_row)
    
visited = [False] * len(chick_list)
min_length = sys.maxsize
dfs(0, 0) # 고른 개수, 현재 치킨집 체크
print(min_length)