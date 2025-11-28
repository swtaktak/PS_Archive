# 14552_new
import sys
input = sys.stdin.readline
daegi = list(map(int, input().split()))
ans_list = []

# idea
body_list = [[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7], [6,7,8], [7,8,9],
            [1,1,1], [2,2,2], [3,3,3], [4,4,4], [5,5,5], [6,6,6], [7,7,7],
            [8,8,8], [9,9,9]]

pae_cnt = [0 for _ in range(10)]
for d in daegi:
    pae_cnt[d] += 1
        
# step 1. 치또이즈를 확인한다.
two_set = []
one_set = []
for p in range(1, 10):
    if pae_cnt[p] == 2:
        two_set.append(p)
    elif pae_cnt[p] == 1:
        one_set.append(p)
# 치또이즈 확정임
if len(two_set) == 6:
    ans_list.append(one_set[0])
    
# step 2. 그냥 전부 다 돌려
for body1 in body_list:
    for body2 in body_list:
        for body3 in body_list:
            for body4 in body_list:
                for head in range(1, 10):
                    cur_cnt = [0 for _ in range(10)]
                    for b in body1:
                        cur_cnt[b] += 1
                    for b in body2:
                        cur_cnt[b] += 1
                    for b in body3:
                        cur_cnt[b] += 1
                    for b in body4:
                        cur_cnt[b] += 1
                    cur_cnt[head] += 2
                    
                    need = []
                    is_valid = True
                    for i in range(1, 10):
                        if cur_cnt[i] < pae_cnt[i]:
                            is_valid = False
                            break
                        diff = cur_cnt[i] - pae_cnt[i]
                        if diff == 1:
                            need.append(i)
                        elif diff > 1:
                            is_valid = False
                            break
                    if is_valid and len(need) == 1:
                        wait = need[0]
                        if pae_cnt[wait] < 4:
                            if wait not in ans_list:
                                ans_list.append(wait)                             
                
if len(ans_list) == 0:
    print(-1)
else:
    ans_list.sort()
    for a in ans_list:
        print(a, end = " ")