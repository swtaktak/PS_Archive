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
            diff_list.append(cur_diff)
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
            # 차이는 2 이상이 불가능하다. 음수도 불가능
            if diff_set[1] - diff_set[0] >= 2 or diff_set[0] < 0:
                print(-1)
            else:
                # 초항이 정수이므로 처음부터 반복될 수 밖에 없음.
                repeat_list = []
                for cur_len in range(1, len(diff_list) + 1):
                    cur_seg = diff_list[:cur_len]
                    cur_repeat_flag = True
                    for j in range(cur_len, len(diff_list) + 1, cur_len):
                        if j + cur_len <= len(diff_list):
                            cur_comp = diff_list[j:j+cur_len]
                            if cur_seg != cur_comp:
                                cur_repeat_flag = False
                                break
                        else:
                            cur_comp = diff_list[j:len(diff_list)]
                            final_len = len(diff_list) - j
                            if cur_comp != diff_list[:final_len]:
                                cur_repeat_flag = False
                                break
                    if cur_repeat_flag:
                        repeat_list.append(cur_len)
                # 반복 후보 중 되는게 있는가?
                for div in repeat_list:
                    success_flag = True
                    sumed = sum(diff_list[:div])
                    for i in range(1, N+1):
                        cur_num = a0 + (sumed * i) // div
                        if cur_num != num_list[i]:
                            success_flag = False
                            break
                    if success_flag:
                        ans = min(ans, sumed/div)
                if ans != 10 ** 7:
                    print(ans)
                else:
                    print(-1)