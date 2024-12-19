# PROBRAIN, GROW, ARGOS, ADMIN, ANT, MOTION, SPG, COMON, ALMIGHTY
import sys
input = sys.stdin.readline
union_name = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']
cand_solved = []

N = int(input())
for _ in range(len(union_name)):
    cur_row = list(map(int, input().split()))
    cand_solved.append(max(cur_row))

max_idx = cand_solved.index(max(cand_solved))
print(union_name[max_idx])