import sys
from collections import deque
import copy
input = sys.stdin.readline
def dfs(level, ans):
    if level == 9:
        cur_puzzle = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            r = i // 3
            c = i % 3
            cur_puzzle[r][c] = ans[i]
        puzzle_dict[cur_puzzle] = False
        return
    else:
        for i in range(0, 9):
            if not visited[i]:
                ans += str(i)
                visited[i] = True
                dfs(level + 1, ans)
                ans = ans[:-1]
                visited[i] = False


# step 1 / vistied 저장할 dict를 만든다.
puzzle_dict = {}
visited = [False] * 9
dfs(0, '')

start_pos = []
for _ in range(3):
    start_pos.append(list(map(int, input().split())))
goal_pos = '123456780'

# step 2 / 하나씩 움직여서 판단한다.
q = deque()
q.append([0, start_pos])
answer = -1
while q:
    # 2-1 정답 확인
    cur_turn, cur_puzz = q.popleft()
    if cur_puzz == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
        answer = cur_turn
        break
    # 2-2 방문 처리 후 판단.
    puzzle_dict[cur_puzz] = True
    # zero 위치 판단.
    for i in range(3):
        for j in range(3):
            if cur_puzz[i][j] == 0:
                zx, zy = i, j
    # 0을 left move
    if zx - 1 >= 0:
        left_copy = copy.deepcopy(cur_puzz)
        left_copy[zx-1][zy], left_copy[zx][zy] = left_copy[zx][zy], left_copy[zx-1][zy]
        if not puzzle_dict[left_copy]:
            puzzle_dict[left_copy] = True
            q.append([cur_turn + 1, left_copy])
        # 0을 right move
    if zx + 1 < 3:
        right_copy = copy.deepcopy(cur_puzz)
        right_copy[zx+1][zy], right_copy[zx][zy] = right_copy[zx][zy], right_copy[zx+1][zy]
        if not puzzle_dict[right_copy]:
            puzzle_dict[right_copy] = True
            q.append([cur_turn + 1, right_copy])
        # 0을 up move
    if zy - 1 >= 0:
        up_copy = copy.deepcopy(cur_puzz)
        up_copy[zx][zy-1], up_copy[zx][zy] = up_copy[zx][zy], up_copy[zx][zy-1]
        if not puzzle_dict[up_copy]:
            puzzle_dict[up_copy] = True
            q.append([cur_turn + 1, up_copy])
        # 0을 left move
    if zy + 1 < 3:
        down_copy = copy.deepcopy(cur_puzz)
        down_copy[zx][zy+1], down_copy[zx][zy] = down_copy[zx][zy], down_copy[zx][zy+1]
        if not puzzle_dict[down_copy]:
            puzzle_dict[down_copy] = True
            q.append([cur_turn + 1, down_copy])
print(answer)