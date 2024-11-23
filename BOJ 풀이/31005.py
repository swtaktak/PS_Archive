import sys
from collections import deque
input = sys.stdin.readline
bugs, fruits = map(int, input().split())
num_list = list(map(int, input().split()))
left_fruit  = fruits % sum(num_list)
queue = deque()
left_bug_sum = 0
for n in num_list:
    if n <= left_fruit:
        queue.append(n)
        left_bug_sum += n
# 우선 나머지로 모두 다 돌 수 있게 처리를 한번 하자.

# queue = 0 -> 애초에 아무도 이제 못먹는다.
if len(queue) == 0:
    print(left_fruit)
else:
    left_cycle_cnt = left_fruit // left_bug_sum
    left_fruit = left_fruit - left_cycle_cnt * left_bug_sum

    while len(queue) > 1:
        cur_bug = queue.popleft()
        if cur_bug <= left_fruit:
            left_fruit -= cur_bug
            queue.append(cur_bug)
        else:
            # 못 가져갈 경우에는 곰곰이 명단에서 빼고 합산에서도 뺜다.
            left_bug_sum -= cur_bug
            # 반복 안 시키게 나머지 계산을 시킨다.
            if left_bug_sum > 0:
                left_fruit %= left_bug_sum
        # 곰곰이 전원 탈락 / 과일 없음
        if left_fruit == 0 or left_bug_sum == 0:
            break
    # 과일을 다 먹어서 끝남.
    if left_fruit == 0:
        print(0)
    # 모든 곰곰이가 못먹는다. 나머지를 준다.
    elif left_bug_sum == 0:
        print(left_fruit)
    # 딱 한마리 남은건 최소값일 것이다. 무조건. 혼자 계속 그 개수 가져가게. 
    else:
        print (left_fruit % queue[0])