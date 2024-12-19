import sys
input = sys.stdin.readline
rank_num, pool_time, rank_sectors = map(int, input().split())
def print_list(l):
    for cur_l in l:
        print(cur_l, end = " ")
    print()
# base에서 변형을 가하고자 한다.
base_rank = [i for i in range(1, rank_num + 1)]    
# 만일 같은 등수 그룹이 없다면
if rank_sectors == 0:
    another_rank = [i for i in range(rank_num + 1, 2 * rank_num + 1)]
# 만일 같은 등수 그룹이 있다면
else:
    sector_list = list(map(int, input().split()))
    another_rank = []
    for i in range(rank_sectors):
        # 한 칸씩 밀어낼 그룹을 결정한다.
        if i == 0:
            cur_sector = base_rank[:sector_list[i]]
        else:
            cur_sector = base_rank[sector_list[i-1]:sector_list[i]]
            
        if len(cur_sector) == 1:
            another_rank.append(cur_sector[0])
        else:
            sector_move = cur_sector[1:] + [cur_sector[0]]
            for s in sector_move :
                another_rank.append(s)
    if sector_list and sector_list[-1] != rank_num:
        add_diff = rank_num - sector_list[-1]
        add_list = [i for i in range(rank_num + 1, rank_num + 1 + add_diff)]
        another_rank += add_list

for i in range(pool_time):
    if i == 0:
        print_list(base_rank)
    else:
        print_list(another_rank)