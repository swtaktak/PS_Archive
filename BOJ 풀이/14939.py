import sys
import copy
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
input = sys.stdin.readline
bulb_map = []

def get_binary(x):
    ans = ''
    while x > 0:
        ans += str(x % 2)
        x = x // 2
    ans = ans + ('0' * (10 - len(ans)))
    return ans[::-1]

for _ in range(10):
    cur_row = list(str(input().rstrip()))
    cur_row_num = []
    for i in range(10):
        if cur_row[i] == '#':
            cur_row_num.append(0)
        else:
            cur_row_num.append(1)
    bulb_map.append(cur_row_num)

min_answer = 101
success_flag = False
for first_press in range(0, 1024):
    cur_map = copy.deepcopy(bulb_map)
    first_row = get_binary(first_press)
    cur_press = 0
    # 첫 번째 줄에 대해서 : 모두 다 백트래킹을 실시한다.
    for c in range(0, 10):
        if first_row[c] == '1':
            cur_press += 1
            cur_r = 0
            cur_c = c
            cur_map[cur_r][cur_c] = 1 - cur_map[cur_r][cur_c]
            for mv in mv_list:
                nr = cur_r + mv[0]
                nc = cur_c + mv[1]
                if 0 <= nr < 10 and 0 <= nc < 10:
                    cur_map[nr][nc] = 1 - cur_map[nr][nc]
    # 두 번째 줄부터, 자신의 위가 불이켜져 있으면 눌러라.
    for r in range(1, 10):
        for c in range(0, 10):
            if cur_map[r-1][c] == 1:
                cur_press += 1
                cur_map[r][c] = 1 - cur_map[r][c]
                for mv in mv_list:
                    nr = r + mv[0]
                    nc = c + mv[1]
                    if 0 <= nr < 10 and 0 <= nc < 10:
                        cur_map[nr][nc] = 1 - cur_map[nr][nc]
    # 전부 다 켜졌는가?
    cur_success_flag = True
    for r in range(0, 10):
        for j in range(0, 10):
            if cur_map[r][j] == 1:
                cur_success_flag = False
    if cur_success_flag:
        success_flag = True
        min_answer = min(min_answer, cur_press)
                
if success_flag:
    print(min_answer)
else:
    print(-1)