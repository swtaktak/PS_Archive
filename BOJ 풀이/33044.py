import sys
import math
input = sys.stdin.readline

def pae_dfs(level, cur_pos):
    if level == 4:
        right_body_flag = True
        for i in range(1, 10):
            if cur_cnt[i] >= 5:
                right_body_flag = False
                break
        if right_body_flag:
            for i in range(1, 10):
                if cur_cnt[i] <= 2:
                    cur_cnt[i] += 2
                    cur_pae = "".join([str(x) for x in cur_cnt])
                    pos_set.add(cur_pae)
                    cur_cnt[i] -= 2
        return
    for i in range(cur_pos, len(body_list)):
        for b in body_list[i]:
            cur_cnt[b] += 1
        pae_dfs(level + 1, i)
        for b in body_list[i]:
            cur_cnt[b] -= 1
                
def seven_head_dfs(level, cur_pos):
    if level == 7:
        cur_cnt_seven = [0] * 10
        for c in cur_pick:
            cur_cnt_seven[c] += 2
        cur_pae = "".join([str(x) for x in cur_cnt_seven])
        pos_set.add(cur_pae)
            
        return
    for i in range(cur_pos, 10):
        if not visited_seven_body[i]:
            visited_seven_body[i] = True
            cur_pick.append(i)
            seven_head_dfs(level + 1, i)
            visited_seven_body[i] = False
            cur_pick.pop()
            
def nCk(have, need):
    if have == 0:
        return 1
    elif need == 0:
        return 1
    else:
        return math.factorial(have) // (math.factorial(need) * math.factorial(have - need))

N = int(input())
pae_list = list(map(int, input().split()))
pae_cnt = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for p in pae_list:
    pae_cnt[p] += 1

body_list = [[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7], [6,7,8], [7,8,9],
            [1,1,1], [2,2,2], [3,3,3], [4,4,4], [5,5,5], [6,6,6], [7,7,7],
            [8,8,8], [9,9,9]]
pos_set = set()
# pos_set에 가능한 원소를 모두 저장해보자. 해봤자 1만개 정도다.
cur_cnt = [0] * 10
pae_dfs(0, 0)
# 치또이즈를 하자.
visited_seven_body = [False] * 10
cur_pick = []
seven_head_dfs(0, 1)
pos_set = list(pos_set)
# 각 pos_set 
answer = 0
for cur_p in pos_set:
    cur_list = [int(x) for x in cur_p]
    is_valid = True
    # cur_list의 개수만큼 가지고 있는가
    for i in range(1, 10):
        if cur_list[i] > 0:
            if pae_cnt[i] < cur_list[i]:
                is_valid = False
                break
    if is_valid:
        cur_cnt = 1
        for i in range(1, 10):
            need = cur_list[i]
            have = pae_cnt[i]
            cur_cnt *= nCk(have, need)
        answer += cur_cnt
print(answer)