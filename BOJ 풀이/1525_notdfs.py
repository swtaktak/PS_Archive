import sys
from collections import deque
input = sys.stdin.readline

def puzzle_to_str(puzz):
    ans = ''
    for i in range(3):
        for j in range(3):
            ans += str(puzz[i][j])
    return str(ans)

# step 1 / vistied 저장할 dict를 만든다.
puzzle_dict = []
start_pos = []
for _ in range(3):
    start_pos.append(list(map(int, input().split())))
goal_pos = '123456780'

# step 2 / 하나씩 움직여서 판단한다.
q = deque()
start_str = puzzle_to_str(start_pos)
q.append([0, start_str])
answer = -1
while q:
    # 2-1 정답 확인
    cur_turn, cur_puzz = q.popleft()
    if cur_puzz == goal_pos:
        answer = cur_turn
        break
    # 하나씩 바뀐거는 불가능이라. 그거를 fail case로 넣어둬서 실패 판단 빠르게
    elif cur_puzz in ['123456870', '213456780', '132456780', '124356780', '123546780', '123465780', '123457680',
                          '423156780', '123756480', '153426780', '123486750', '126453780', '173456280', '128456730']:
        answer = -1
        break
    # 2-2 방문 처리 후 이동 파트
    puzzle_dict.append(cur_puzz)
    zero_pos = cur_puzz.index('0')
    # 아래와 변경 가능
    if zero_pos in [0, 1, 2, 3, 4, 5]:
        new_answer = ''
        for i in range(9):
            if i == zero_pos:
                new_answer += cur_puzz[i + 3]
            elif i == zero_pos + 3:
                new_answer += cur_puzz[i - 3]
            else:
                new_answer += cur_puzz[i]
        if new_answer not in puzzle_dict:
            puzzle_dict.append(new_answer)
            q.append([cur_turn + 1, new_answer])
    # 위와 변경 가능
    if zero_pos in [3, 4, 5, 6, 7, 8]:
        new_answer = ''
        for i in range(9):
            if i == zero_pos:
                new_answer += cur_puzz[i - 3]
            elif i == zero_pos - 3:
                new_answer += cur_puzz[i + 3]
            else:
                new_answer += cur_puzz[i]
        if new_answer not in puzzle_dict:
            puzzle_dict.append(new_answer)
            q.append([cur_turn + 1, new_answer])
    # 왼쪽과 변경 가능
    if zero_pos in [1, 2, 4, 5, 7, 8]:
        new_answer = ''
        for i in range(9):
            if i == zero_pos:
                new_answer += cur_puzz[i - 1]
            elif i == zero_pos - 1:
                new_answer += cur_puzz[i + 1]
            else:
                new_answer += cur_puzz[i]
        if new_answer not in puzzle_dict:
            puzzle_dict.append(new_answer)
            q.append([cur_turn + 1, new_answer])
    # 오른쪽과 변경 가능
    if zero_pos in [0, 1, 3, 4, 6, 7]:
        new_answer = ''
        for i in range(9):
            if i == zero_pos:
                new_answer += cur_puzz[i + 1]
            elif i == zero_pos + 1:
                new_answer += cur_puzz[i - 1]
            else:
                new_answer += cur_puzz[i]
        if new_answer not in puzzle_dict:
            puzzle_dict.append(new_answer)
            q.append([cur_turn + 1, new_answer])
print(answer)