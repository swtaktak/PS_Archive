# 32207
import sys
input = sys.stdin.readline
mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]
def not_nb(pick_list):
    for p in pick_list:
        cx, cy = p[1], p[2]
        for mv in mv_list:
            nx, ny = cx + mv[0], cy + mv[1]
            for p in pick_list:
                if p[1] == nx and p[2] == ny:
                    return False
    return True

def dfs(level, cur_pos):
    global max_ans
    if level > pick_max:
        return
    elif 0 < level <= pick_max:
        if not_nb(pick_list):
            cur_sum = 0
            for p in pick_list:
                cur_sum += p[0]
            if cur_sum > max_ans:
                max_ans = cur_sum
    for i in range(cur_pos, len(ruby_list)):
        if not visited[i]:
            visited[i] = True
            pick_list.append(ruby_list[i])
            dfs(level + 1, i)
            visited[i] = False
            pick_list.pop()

rows, cols, pick_max = map(int, input().split())
ruby_list = []
for i in range(rows):
    cur_row = list(map(int, input().split()))
    for j in range(cols):
        ruby_list.append([cur_row[j], i, j])
ruby_list.sort(key = lambda x: x[0], reverse = True)
max_len = min(pick_max * 5, len(ruby_list))
ruby_list = ruby_list[:max_len]
visited = [False for _ in range(len(ruby_list))]
pick_list = []
max_ans = 0
dfs(0, 0)
print(max_ans)5배 컷으로 잡았기 한데..