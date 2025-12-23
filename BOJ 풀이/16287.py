import sys
input = sys.stdin.readline

goal, N = map(int, input().split())
w_list = list(map(int, input().split()))

w_list.sort()
combi_dict = {}

for w1 in range(0, N-1):
    for w2 in range(w1 + 1, N):
        if w1 != w2:
            cur_weight = w_list[w1] + w_list[w2]
            combi_dict[cur_weight] = [w1, w2]
success_flag = False
for cur_w in range(3, goal):
    if cur_w in combi_dict and goal - cur_w in combi_dict:
        w1 = combi_dict[cur_w][0]
        w2 = combi_dict[cur_w][1]
        if w1 not in combi_dict[goal - cur_w] and w2 not in combi_dict[goal - cur_w]:
            success_flag = True
            break

if success_flag:
    print('YES')
else:
    print('NO')