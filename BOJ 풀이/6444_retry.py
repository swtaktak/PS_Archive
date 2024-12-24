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
    cur_c = 0
    alphas = alphas[::-1]
    for i in range(len(alphas)):
        cur_c += (26 ** i) * (ord(alphas[i]) - 64)
    cur_c -= 1
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
    graph = {}
    indegree_map = {}
    
    for r in range(rows):
        for c in range(cols):
            if '=' not in sheet[r][c]:
                answer[r][c] = int(sheet[r][c])
            elif '+' in sheet[r][c]:
                sum_coord_list = list(sheet[r][c][1:].split('+'))
                for s in sum_coord_list:
                    cr, cc = get_coord(s)
                    # 보려는게 숫자일 경우 추가하지 말고 여기서 바로 직접 연결하자.
                    if '=' not in sheet[cr][cc]:
                        answer[r][c] += int(sheet[cr][cc])
                    else:
                        if (cr, cc) not in graph:
                            graph[(cr, cc)] = [(r, c)]
                        else:
                            graph[(cr, cc)].append((r, c))
            else:
                cr, cc = get_coord(sheet[r][c][1:])
                if '=' not in sheet[cr][cc]:
                    answer[r][c] += int(sheet[cr][cc])
                else:
                    if (cr, cc) not in graph:
                        graph[(cr, cc)] = [(r, c)]
                    else:
                        graph[(cr, cc)].append((r, c))
    # 다음 그래프를 바탕으로 indegree_map을 구하자.
    for cur_v in graph:
        if cur_v not in indegree_map:
            indegree_map[cur_v] = 0
        for nv in graph[cur_v]:
            if nv not in indegree_map:
                indegree_map[nv] = 1
            else:
                indegree_map[nv] += 1
                
    q = deque()
    for cur_v in indegree_map:
        cr, cc = cur_v[0], cur_v[1]
        if indegree_map[cur_v] == 0:
            q.append([cr, cc])
    while q:
        cr, cc = q.popleft()
        if (cr, cc) in graph:
            nv_list = graph[(cr, cc)]
            for nv in nv_list:
                nr, nc = nv[0], nv[1]
                answer[nr][nc] += answer[cr][cc]
                indegree_map[(nr, nc)] -= 1
                if indegree_map[(nr, nc)] == 0:
                    q.append([nr, nc])
    for r in range(rows):
        for c in range(cols):
            print(answer[r][c], end = " ")
        print()