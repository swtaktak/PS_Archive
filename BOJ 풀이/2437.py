import sys
input = sys.stdin.readline

N = int(input())
w_list = list(map(int, input().split()))
w_list.sort()

goal = 1
answer = 0
for i in range(N):
    if i == 0:
        if w_list[i] >= 2:
            answer = 1
            break
        else:
            goal += 1
    else:
        # 현재 무게가 택도 없이 클때
        if w_list[i] > goal:
            answer = goal
            break
        else:
            goal = goal + w_list[i]
if goal > sum(w_list):
    print(goal)
else:
    print(answer)