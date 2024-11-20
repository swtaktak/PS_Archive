# 1210 사다리문제
# import sys
# input = sys.stdin.readline
t_case = 10
N = 100

for _ in range(1, t_case + 1):
    answer = 0
    cur_test = int(input())
    ladder_map = []
    ladder_start = []
    swap_result = []
    for i in range(N):
        cur_row = list(map(int, input().split()))
        if i == 0:
            vertical_cnt = 0
            for j in range(N):
                if cur_row[j] == 1:
                    ladder_start.append(j)
                    swap_result.append(vertical_cnt)
                    vertical_cnt += 1
                    # swap result에서 2를 찾으면 됨.
            # 뻗어나갈 가지의 위치를 체크한다.
            swap_check_pos = [x+1 for x in ladder_start[:-1]]
        elif i < N-1:
            for j in swap_check_pos:
                if cur_row[j] == 1:
                    left_idx = ladder_start.index(j - 1)
                    swap_result[left_idx], swap_result[left_idx + 1] = swap_result[left_idx + 1], swap_result[left_idx]
        else:
            for j in range(N):
                if cur_row[j] == 2:
                    arrive_pos = ladder_start.index(j)
                    swap_pos = swap_result[arrive_pos]
                    answer = ladder_start[swap_pos]
    
    print("#%d %d" %(cur_test, answer))