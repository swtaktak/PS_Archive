# 도서관
# 양수 방향과 음수 방향을 별도로 나눠 처리.
import sys
input = sys.stdin.readline
book, hand = map(int, input().split())
goal_list = list(map(int, input().split()))

plus_list = []
minus_list = []
for g in goal_list:
    if g > 0:
        plus_list.append(g)
    elif g < 0:
        minus_list.append(g)
plus_list.sort(reverse = True) # 플러스는 큰 거부터 묶는다.
minus_list.sort(reverse = False) # 마이너스는 작은 거부터 묶는다.
goal = []
# 플 마가 섞이는거? 사실 왕복 서로 찍어야 해서 나눠 드는거랑 큰 차이가 없다.
for i in range(0, len(plus_list), hand):
    end_point = min(i+hand, len(plus_list))
    cur_list = plus_list[i:end_point]
    goal.append(cur_list[0])
for i in range(0, len(minus_list), hand):
    end_point = min(i+hand, len(minus_list))
    cur_list = minus_list[i:end_point]
    goal.append(-cur_list[0])
goal.sort(reverse = False)
answer = 0
for i in range(len(goal)):
    if i != len(goal)-1:
        answer += 2*goal[i]
    else:
        answer += goal[i]
print(answer)