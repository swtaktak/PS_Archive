import sys
input = sys.stdin.readline

N = int(input())
total_com = 0
switch_list = []
for i in range(N):
    hole, cost = map(int, input().split())
    switch_list.append([hole - 1, cost])
    total_com += (hole - 1)

need_com = int(input())

if need_com > total_com:
    print(-1)
else:
    INF = 1e18
    dp_list = [INF] * (need_com + 1)
    dp_list[0] = 0
    
    switch_list.sort(key = lambda x:[x[1], -x[0]])
    for i in range(N):
        if i == 0:
            cur_hole, cur_cost = switch_list[i][0], switch_list[i][1]
            for j in range(1, cur_hole + 1):
                dp_list[ㅓ] = cur_cost
        else:
            #뭔가 이상해! ㅠㅠㅠ