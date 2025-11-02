import sys
from collections import deque
input = sys.stdin.readline

def bfs(sr, sc, lv):
    q = deque()
    q.append([sr, sc, lv])
    
    while q:
        cr, cc, clv = q.popleft()
        if clv == 2:
            ans = col_dict_rev[cc + 1] + str(cr + 1)
            if ans not in ans_list:
                ans_list.append(ans)
        else:
            for mv in mv_list:
                nr, nc = cr + mv[0], cc + mv[1]
                if 0 <= nr < 8 and 0 <= nc < 8:
                    q.append([nr, nc, clv + 1])
            
mv_list = [[-2, 1], [-2, -1], [2, 1], [2, -1],
           [-1, 2], [-1, -2], [1, 2], [1, -2]]
col_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
col_dict_rev = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}

start_pos = str(input().rstrip())
sr = int(start_pos[1]) - 1
sc = col_dict[start_pos[0]] - 1
ans_list = []

bfs(sr, sc, 0)

for a in ans_list:
    print(a)