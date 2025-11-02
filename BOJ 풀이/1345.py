# 문제 조건상, 공차는 0보다 커야 하다.
import sys
input = sys.stdin.readline
N, a0 = map(int, input().split())
ans = 10 ** 7
if N == 0:
    print(0)
else:
    num_list = [a0] + list(map(int, input().split()))
    # 항이 두개인 경우에 대하여여
    if N == 1:
        if num_list[0] > num_list[1]:
            print(-1)
        else:
            print(num_list[1] - num_list[0])
    else:
        # 항이 3개 이상인 경우에 대하여는 공차를 본다.
        # 공차의 종류와 길이를 모두 담기 위해 분류해서 담자.
        diff_list = []
        diff_set = []
        for i in range(1, N + 1):
            cur_diff = num_list[i] - num_list[i-1]
            if cur_diff not in diff_set:
                diff_set.append(cur_diff)
            if len(diff_list) == 0:
                diff_list.append([cur_diff, 1])
            else:
                if diff_list[-1][0] != cur_diff:
                    diff_list.append([cur_diff, 1])
                else:
                    diff_list[-1][1] += 1
        # 차이가 3 종류 이상 불가.
        if len(diff_set) >= 3:
            print(-1)
        # 차이가 1 종류일 경우우
        elif len(diff_set) == 1:
            if diff_set[0] >= 0:
                print(diff_set[0])
            else:
                print(-1)
        # 차이가 2 종류일 경우
        else:
            if max(diff_set) - min(diff_set) != 1:
                print(-1)
            else:
                ans_cand = (diff_list[0][0] * diff_list[0][1] + diff_list[1][0] * diff_list[1][1]) / (diff_list[0][1] + diff_list[1][1])
                # 하지만 개판인 경우를 대비해야 한다. (삑사리 대비)
                success_flag = True # 실패의 경우
                less_flag = False # 길이가 부족할땐 탐색 마무리 해야함. 더 있으면 오류
                for i in range(2, len(diff_list)):
                    cur_diff_cnt = diff_list[i][1]
                    if less_flag:
                        success_flag = True
                        break
                    elif i % 2 == 0:
                        if diff_list[0][1] < cur_diff_cnt:
                            success_flag = False
                            break
                        elif diff_list[0][1] > cur_diff_cnt:
                            less_flag = True
                    elif i % 2 == 1:
                        if diff_list[1][1] < cur_diff_cnt:
                            success_flag = False
                            break
                        elif diff_list[1][1] > cur_diff_cnt:
                            less_flag = True
                if success_flag:
                    print(ans_cand)
                else:
                    print(-1)