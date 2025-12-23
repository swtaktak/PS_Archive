import sys
input = sys.stdin.readline
INF = 100001
# L1 norm이 가장 작은 애를 매 순간 그리디하게 뽑을 것이다.
# 사실 더 그리디하게 항상 봐야 하는데... 음... 맵 크기 대비 빡빡하지 않아서
# L1 norm만 봐도 무방할 것이다.
def dist(x1, y1, x2, y2):
    return abs(x1- x2) + abs(y1 - y2)

rows, cols, id_len = map(int, input().split())

# 지도를 만든다.
# 글자별 개수를 세고, 글자별 위치 또한 포함한다.
char_cnt = {}
char_pos_list = {}
for r in range(rows):
    cur_row = list(input().rstrip())
    for c in range(cols):
        if cur_row[c] not in char_pos_list:
            char_pos_list[cur_row[c]] = [[r, c]]
            char_cnt[cur_row[c]] = 1
        else:
            char_pos_list[cur_row[c]].append([r, c])
            char_cnt[cur_row[c]] += 1
id = str(input().rstrip())

# 이제 아이디의 글자를 센다.
id_cnt = {}
for i in id:
    if i not in id_cnt:
        id_cnt[i] = 1
    else:
        id_cnt[i] += 1

# 이제 최대 몇 억을 벌 수 있는지 센다.
# 이것은 100만번의 트라이는 고려하지 않는다.
max_try = INF
is_possible = True
for cur_i in id_cnt:
    if cur_i not in char_cnt:
        is_possible = False
        break
    else:
        max_try = min(max_try, char_cnt[cur_i] // id_cnt[cur_i])

# 가능 횟수가 0번이거나 애초에 상금 가능이 0억일 경우.
# 시도도 하지 말고 던전을 빠져 나가라.
if max_try == 0 or not is_possible:
    step = (rows - 1) + (cols - 1)
    print("%d %d" % (0, step))
    print("R" * (cols -1 ) + 'D' * (rows - 1))
    
else:
    # history에 들어가는 것은 이동 문자열()
    # pop 보다는 visited 판단이 더 빠름
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    history = []
    cr, cc = 0, 0
    cur_turn = 0
    cur_try = 0
    while cur_try < max_try:
        cur_try_command = ''
        for cur_i in id:
            min_dist = INF
            nr = cr
            nc = cc
            for cand_r, cand_c in char_pos_list[cur_i]:
                if not visited[cand_r][cand_c]:
                    cur_dist = dist(cr, cc, cand_r, cand_c)
                    if min_dist > cur_dist:
                        min_dist = cur_dist
                        nr = cand_r
                        nc = cand_c
            # nr, nc가 다음 갈 곳임.
            visited[nr][nc] = True
            cur_turn += min_dist
            # 좌우 이동 먼저
            if cr < nr:
                cur_try_command += ('D' * (nr - cr))
            if cr > nr:
                cur_try_command += ('U' * (cr - nr))
            if cc < nc:
                cur_try_command += ('R' * (nc - cc))             
            if cc > nc:
                cur_try_command += ('L' * (cc - nc))   
            # 이제 템을 줍는다.
            cur_try_command += 'P'
            cur_turn += 1
            # 현재 위치를 저장한다.
            cr = nr
            cc = nc
        # 현재 위치에서 탈출을 먼저 감행한다.
        if cur_turn + (rows - cr - 1) + (cols - cc - 1) > 1000000:
            break
        else:
            # 지금까지의 커맨드와 현재 위치를 저장하고 다음으로 넘어간다.
            # 성공적으로 상금 1억을 얻게 된다. 그러나 아직 탈출이 아니다.
            history.append([cur_try_command, (cr, cc)])
            cur_try += 1
            
    # 이제 상금과 최종 커멘트를 입력한다.
    # 상금은 cur_try
    if cur_try == 0:
        step = (rows - 1) + (cols - 1)
        print("%d %d" % (0, step))
        print("R" * (cols -1 ) + 'D' * (rows - 1))
    else:
        ans_hist = ''
        for i in range(0, cur_try):
            ans_hist += history[i][0]
            if i == cur_try -1:
                cr, cc = history[i][1]
                ans_hist += (("R" * (cols - cc - 1) + "D" * (rows - cr - 1)))
        cur_turn += ((cols - cc - 1) + (rows - cr - 1))
        print("%d %d" % (cur_try, cur_turn))
        print(ans_hist)