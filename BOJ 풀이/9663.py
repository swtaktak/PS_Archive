# Claassical DFS 문제 : N-queen
def dfs(cur_queen):
    global count
    
    # 성공적으로 N개를 놨다면
    if cur_queen == N:
        count += 1
    # dfs 진행 필요 (퀸이 부족)
    else:
        for i in range(N):
            col_pos[cur_queen] = i
            if is_it_right(col_pos, cur_queen):
                # 맞을 경우 진행
                # 이번의 경우는 위치 갱신이나 제거가 필요 없음
                # 어차피 성공/실패 상관없이 상단의 for에서 다음거 자동 감.
                dfs(cur_queen + 1)

def is_it_right(col_pos, cur_queen):
    if cur_queen == 0:
        return True
    else:
        cur_pos = col_pos[cur_queen]
        # 이전의 queen에 대해 체크한다.
        for prev_queen in range(0, cur_queen):
            if col_pos[prev_queen] == cur_pos:
                return False
            elif cur_queen - prev_queen == abs(col_pos[cur_queen] - col_pos[prev_queen]):
                return False
        return True
            
N = int(input())
col_pos = [-1] * (N)
count = 0
dfs(0)
print(count)