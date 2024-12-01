# 해 구성 문제 시도
import sys
input = sys.stdin.readline
rank_num, pool_time, rank_sectors = map(int, input().split())
def print_list(l):
    for i in range(len(l)):
        if i < len(l)-1:
            print(l[i], end = " ")
        else:
            print(l[i])
if rank_sectors > 0:
    sector_list = list(map(int, input().split()))
    group_person = []
    for i in range(rank_sectors):
        if i == 0:
            group_person.append(sector_list[i])
        else:
            group_person.append(sector_list[i] - sector_list[i-1])
    if rank_num - sector_list[-1] > 0:
        group_person.append(rank_num - sector_list[-1])
        
# 해 출력 부분 Part 1 / 같은 순위 조합이 없어야 할 경우
# 틀어버린다
if rank_sectors == 0:
    for i in range(pool_time):
        if i == 0:
            rank_list = [j for j in range(1, rank_num+ 1)]
            print_list(rank_list)
        else:
            rank_list = [i + j + 1 for j in range(1, rank_num + 1)]
            print_list(rank_list)
else:
    for i in range(pool_time):
        if i != 0:
            # 최초가 아니라면 그냥 밀어도 됨
            rank_list = [i for i in range(1, rank_num+ 1)]
            # 마지막에 바꿔줘야할 사람이 남을 때
            if rank_num != sector_list[-1]:
                rank_list[-1] += 1
            print_list(rank_list)
        elif i == 0:
            rank_list = [i+1 for i in range(1, rank_num + 1)]
            sum = 0
            for c in group_person:
                sum += c
                rank_list[sum-1] -= c  
            print_list(rank_list)