# idea : 현재의 값을 리스트에 넣는다. 위치를 찾아서 넣자.
# right 위치를 바꾼다.

import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
answer_list = [-1000000001]

def binary_search(answer_list, cur_num):
    left = 0
    right = len(answer_list)
    while left < right:
        mid = (left + right) // 2
        cur_comparision = answer_list[mid]
        # 만일 지금 정답에 있는 숫자보다, 넣어야 하는 수가 더 크다면 왼쪽 포인터 당기기
        if cur_comparision < cur_num :
            left = mid + 1
        else:
            right = mid
    return right

for i in range(N):
    if i == 0:
        answer_list.append(num_list[i])
    else:
        # 순서대로 넣는다. 단, 정확히 현재 수보다 가장 덜 큰 값을 바꾸면 된다.
        cur_num = num_list[i]
        right = binary_search(answer_list, cur_num)
        if right == len(answer_list):
            answer_list.append(cur_num)
        else:
            answer_list[right] = cur_num
print(len(answer_list) - 1)