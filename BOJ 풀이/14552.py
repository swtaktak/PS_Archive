import sys
input = sys.stdin.readline
daegi = list(map(int, input().split()))
ans_list = []
sys.setrecursionlimit(10 ** 6)
def dfs(group, check_list):
    if group == 4:
        # 만일 부족한게 딱 한 종류일 경우
        # 그게, 머리로 들어가면 된다.
        # 그리고 이 경우 패가 4장을 넘는 경우를 고려할 필요가 없다. 어차피 머리가 확정이다.
        # 두 종류가 부족하다는 것의 의미는, 머리가 될 수 없다.
        need_list = []
        cur_judge = True
        for i in range(1, 10):
            #  이렇게 비교하면 4장 초과하는 실패 케이스도 무조건 빠짐
            if check_list[i] > pae_cnt[i]:
                cur_judge = False
                break
            elif pae_cnt[i] - check_list[i] == 2:
                need_list.append(i)
        if cur_judge and len(need_list) == 1:
            return True
    
    for i in range(len(body_list)):
        cur_body = body_list[i]
        for c in cur_body:
            check_list[c] += 1
        dfs(group + 1, check_list)
        for c in cur_body:
            check_list[c] -= 1
    return False 

# idea
body_list = [[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7], [6,7,8], [7,8,9],
            [1,1,1], [2,2,2], [3,3,3], [4,4,4], [5,5,5], [6,6,6], [7,7,7],
            [8,8,8], [9,9,9]]

# 치또이즈는 별도로 하고, 16^4 * 9 하면 몇개 안됨.
# 따라서, 그냥 몸통 4개를 찾은 뒤에 남은게 머리인지 보면 됨.
# 패를 dfs로 하면 됨.

pae_cnt = [0 for _ in range(10)]
for d in daegi:
    pae_cnt[d] += 1
        
# step 1. 치또이즈를 확인한다.
two_set = []
one_set = []
for p in range(1, 10):
    if pae_cnt[p] == 2:
        two_set.append(p)
    else:
        one_set.append(p)
# 치또이즈 확정임
if len(two_set) == 6:
    ans_list.append(one_set[0])
    
# step 2. 몸통 4개와 머리가 2개인 상황을 확인한다.
for new_pae in range(1, 10):
    if pae_cnt[new_pae] < 4:
        pae_cnt[new_pae] += 1
        check_list = [0 for _ in range(10)]
        if dfs(0, check_list):
            # 중복 방지
            if new_pae not in ans_list:
                ans_list.append(new_pae)
        pae_cnt[new_pae] -= 1

if len(ans_list) == 0:
    print(-1)
else:
    ans_list.sort()
    for a in ans_list:
        print(a, end = " ")