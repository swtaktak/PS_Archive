import sys
from collections import deque
import copy
input = sys.stdin.readline
def dfs(level, ans):
    if level == 9:
        puzzle_dict[ans] = False
        return
    else:
        for i in range(0, 9):
            if not visited[i]:
                ans += str(i)
                visited[i] = True
                dfs(level + 1, ans)
                ans = ans[:-1]
                visited[i] = False

def puzzle_to_str(puzz):
    ans = ''
    for i in range(3):
        for j in range(3):
            ans += str(puzz[i][j])
    return str(ans)

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
    cur_puzz_str = puzzle_to_str(cur_puzz)
    if cur_puzz_str == goal_pos:
        answer = cur_turn
        break
    # 하나씩 바뀐거는 불가능이라. 그거를 fail case로 넣어둬서 실패 판단 빠르게
    elif cur_puzz_str in ['123456870', '213456780', '132456780', '124356780', '123546780', '123465780', '123457680',
                          '423156780', '123756480', '153426780', '123486750', '126453780', '173456280', '128456730']:
        answer = -1
        break
    # 2-2 방문 처리 후 판단.
    puzzle_dict[cur_puzz_str] = True
    # zero 위치 판단.
    for i in range(3):
        for j in range(3):
            if cur_puzz[i][j] == 0:
                zx, zy = i, j
    # 0을 left move
    if zx - 1 >= 0:
        left_copy = copy.deepcopy(cur_puzz)
        left_copy[zx-1][zy], left_copy[zx][zy] = left_copy[zx][zy], left_copy[zx-1][zy]
        left_str = puzzle_to_str(left_copy)
        if not puzzle_dict[left_str]:
            puzzle_dict[left_str] = True
            q.append([cur_turn + 1, left_copy])
        # 0을 right move
    if zx + 1 < 3:
        right_copy = copy.deepcopy(cur_puzz)
        right_copy[zx+1][zy], right_copy[zx][zy] = right_copy[zx][zy], right_copy[zx+1][zy]
        right_str = puzzle_to_str(right_copy)
        if not puzzle_dict[right_str]:
            puzzle_dict[right_str] = True
            q.append([cur_turn + 1, right_copy])
        # 0을 up move
    if zy - 1 >= 0:
        up_copy = copy.deepcopy(cur_puzz)
        up_copy[zx][zy-1], up_copy[zx][zy] = up_copy[zx][zy], up_copy[zx][zy-1]
        up_str = puzzle_to_str(up_copy)
        if not puzzle_dict[up_str]:
            puzzle_dict[up_str] = True
            q.append([cur_turn + 1, up_copy])
        # 0을 left move
    if zy + 1 < 3:
        down_copy = copy.deepcopy(cur_puzz)
        down_copy[zx][zy+1], down_copy[zx][zy] = down_copy[zx][zy], down_copy[zx][zy+1]
        down_str = puzzle_to_str(down_copy)
        if not puzzle_dict[down_str]:
            puzzle_dict[down_str] = True
            q.append([cur_turn + 1, down_copy])
print(answer)