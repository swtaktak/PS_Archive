import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
# 주 대각선의 방향을 보고
# 부대각선의 방향을 따진다.
# 비숍의 성질 : 흑칸 비숍은 흑칸만 밟는다, 백칸 비숍은 백칸만 밟는다.
def dfs(cur_lv, num_bishop):
    global max_bishop
    if cur_lv >= 2 * b_size - 1:
        max_bishop = max(max_bishop, num_bishop)
        return

    # 레벨이 0부터 2 * b_size - 2
    for i in range(0, cur_lv + 1):
        j = cur_lv - i
        if 0 <= i < b_size and 0 <= j < b_size:
        # 만일 둘 수 있다면면
            if chess[i][j] == 1 and not neg_diag_visit[i-j]:
                neg_diag_visit[i-j] = True
                dfs(cur_lv + 2, num_bishop + 1)
                neg_diag_visit[i-j] = False
        # 둘 수 없이 넘어 가는 경우도
    dfs(cur_lv + 2, num_bishop)

b_size = int(input())
chess = []
for _ in range(b_size):
    cur_row = list(map(int, input().split()))
    chess.append(cur_row)
neg_diag_visit = {}
for i in range(1-b_size, b_size):
    neg_diag_visit[i] = False
answer = 0
max_bishop = 0   
dfs(0, 0)
answer += max_bishop
max_bishop = 0
dfs(1, 0)
answer += max_bishop
print(answer)