import sys
from collections import deque
# 어떻게 메모리 초과를 벗어날 것인가?
# 숫자일 경우 미리 넣어버리자.
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
    sheet = []
    answer = [[0 for _ in range(cols)] for _ in range(rows)]
    for _ in range(rows):
        cur_row = list(map(str, input().rstrip().split()))
        sheet.append(cur_row)
    graph = [[[] for _ in range(cols)] for _ in range(rows)]
    indegree_map = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if '=' not in sheet[r][c]:
                answer[r][c] = int(sheet[r][c])
            elif '+' in sheet[r][c]:
                sum_coord_list = list(sheet[r][c][1:].split('+'))
                for s in sum_coord_list:
                    cr, cc = get_coord(s)
                    # 보려는게 숫자일 경우 추가하지 말고 여기서 바로 직접 연결하자.
                    # 이중 참조만 그래프로 만들자.
                    if '=' not in sheet[cr][cc]:
                        answer[r][c] += int(sheet[cr][cc])
                    else:
                        graph[cr][cc].append([r, c])
                        indegree_map[r][c] += 1
            else:
                cr, cc = get_coord(s)
                if '=' not in sheet[cr][cc]:
                    answer[r][c] += int(sheet[cr][cc])
                else:
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