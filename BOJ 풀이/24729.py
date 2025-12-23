import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

# 계단수를 만들 때 일단 N이 홀수면 실패.
# 맨 앞과 맨 뒤는 1차이 나야해서
# 최소값에서, 출발해서 최솟값 + 1이 되어야 한다.

# 기본적으로 N이 홀수면 실패
# N이 짝수일 경우 최솟값 1개 이상, 최댓값 1개 이상, 그 중간 2개 이상은 확보해야 한다.
# 될 경우, 마지막에 페어 체크를 진행한다.

if N % 2 == 1:
    print(-1)
else:
    min_num = min(num_list)
    max_num = max(num_list)

    cnt_dict = {}
    for n in num_list:
        if n not in cnt_dict:
            cnt_dict[n] = 1
        else:
            cnt_dict[n] += 1
    
    cnt_flag = True
    for i in range(min_num, max_num + 1):
        if i not in cnt_dict:
            cnt_flag = False
            break
        else:
            # 최대치, 최소치는 1번만 등장할 수 있어서
            if i == min_num or i == max_num:
                cnt_dict[i] -= 1
            if min_num < i < max_num:
                if cnt_dict[i] == 1:
                    cnt_flag = False
                    break
                else:
                    # 최대치 최소치가 아닐 경우 한번은 올라갔다 내려와야 하니까 2개를 빼야함
                    # 이 이유는 시작 ~ 끝 차이가 1인 수열이므로. 확정적이다.
                    cnt_dict[i] -= 2
    if not cnt_flag:
        print(-1)
    else:
        # 최소 형태는 확보된다.
        # 나머지는 작은값, 큰값의 계단형 반복이 되나... 보자.
        pair_flag = True
        for i in range(min_num, max_num):
            if cnt_dict[i] > cnt_dict[i + 1]:
                pair_flag = False
                break
            else:
                cnt_dict[i + 1] -= cnt_dict[i]
                cnt_dict[i] = 0
        
        if pair_flag and cnt_dict[max_num] == 0:
            print(1)
        else:
            print(-1) 