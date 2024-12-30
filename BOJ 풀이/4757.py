import sys
input = sys.stdin.readline
# 문제수는 4개로 고정
team = int(input())
# team_name, solve, penalty 계산하여 넣을거임

result = []

for _ in range(team):
    cur_list = list(map(str, input().rstrip().split()))
    cur_team = cur_list[0]
    
    cur_solve = 0
    cur_penalty = 0
    for i in range(1, 9, 2):
        cur_try, solve_time = int(cur_list[i]), int(cur_list[i+1])
        if solve_time > 0:
            cur_penalty += solve_time + (cur_try - 1) * 20
            cur_solve += 1
    result.append([cur_team, cur_solve, cur_penalty])
result.sort(key = lambda x: [x[1], -x[2]], reverse = True)

print("%s %d %d" %(result[0][0], result[0][1], result[0][2]))