import sys
input = sys.stdin.readline
# 10000h + 10000w + 1001o + 1000e + 120l + 100r + d 
weight = [10000, 10000, 1001, 1000, 120, 100, 1]
def dfs(level):
    global answer_pick
    if level == 7:
        if pick[0] != 0 and pick[1] != 0:
            cur_sum = 0
            for i in range(7):
                cur_sum += (pick[i] * weight[i])
            if cur_sum == N:
                answer_pick = pick.copy()
        return
    for i in range(10):
        if not visited[i]:
            visited[i] = True
            pick.append(i)
            dfs(level + 1)
            visited[i] = False
            pick.pop()
N = int(input())

visited = [False] * 10
pick = []
answer_pick = []
dfs(0)

if len(answer_pick) == 0:
    print('No Answer')
else:
    # 10000h + 10000w + 1001o + 1000e + 120l + 100r + d 
    hello = answer_pick[0] * 10000 + answer_pick[3] * 1000 + answer_pick[4] * 110 + answer_pick[2]
    world = answer_pick[1] * 10000 + answer_pick[2] * 1000 + answer_pick[5] * 100 + answer_pick[4] * 10 + answer_pick[6]
    first_line = "  " + str(hello)
    second_line = "+ " + str(world)
    third_line = "-------"
    if N >= 100000:
        fourth_line = " " + str(N)
    else:
        fourth_line = "  " + str(N)
    print(first_line)
    print(second_line)
    print(third_line)
    print(fourth_line)