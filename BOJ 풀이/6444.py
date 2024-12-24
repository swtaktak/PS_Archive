import sys
from collections import deque
input = sys.stdin.readline

def get_coord(s):
    # 엑셀의 번호를 주면, 그거를 전환한다.
    # 알파벳은 26진법으로 A를 1... Z를 26으로 두고...
    # A = 65
    alphas = ''
    nums = ''
    for c in s:
        if c.isalpha():
            alphas += c  # 열 번호
        else:
            nums += c  # 행 번호
    # alpha를 num으로 바꾸자.
    cur_c = 0
    alphas = alphas[::-1]
    for i in range(len(alphas)):
        cur_c += (26 ** i) * (ord(alphas[i]) - 64) - 1
    cur_r = int(nums) - 1
    return [cur_r, cur_c]
    

T = int(input())
for _ in range(T):
    cols, rows = map(int, input().split())
    answer = [[0 for _ in range(cols)] for _ in range(rows)]
    graph = [[[] for _ in range(cols)] for _ in range(rows)]
    indegree_map = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        cur_row = list(map(str, input().rstrip().split()))
        for c in range(cols):
            if '=' not in cur_row[c]:
                answer[r][c] = int(cur_row[c])
            elif '+' in cur_row[c]:
                sum_coord_list = list(cur_row[c][1:].split('+'))
                # 각 좌표를 변형해서, 그래프 rc에 다음 연결점을 추가하고.
                # indegree_list를 1 추가한다.
                # 순환 참조가 발생할 수 없으므로, 위상정렬이 가능하다.
                for s in sum_coord_list:
                    cr, cc = get_coord(s)
                    # 다음 위치를 넣는다.
                    graph[cr][cc].append([r, c])
                    indegree_map[r][c] += 1
            # 하나의 칸을 직접 참조하는 경우
            else:
                cr, cc = get_coord(cur_row[c][1:])
                graph[cr][cc].append([r, c])
                indegree_map[r][c] += 1
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if indegree_map[r][c] == 0:
                q.append([r, c])
    while q:
        cr, cc = q.popleft()
        nv_list = graph[cr][cc]
        for nv in nv_list:
            nr, nc = nv[0], nv[1]
            answer[nr][nc] += answer[cr][cc]
            indegree_map[nr][nc] -= 1
            if indegree_map[nr][nc] == 0:
                q.append([nr, nc])
    for r in range(rows):
        for c in range(cols):
            print(answer[r][c], end = " ")
        print()