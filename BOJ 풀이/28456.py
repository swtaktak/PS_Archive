import sys
import copy
input = sys.stdin.readline

N = int(input())
mt = []
for _ in range(N):
    mt.append(list(map(int, input().split())))
ops = int(input())
for _ in range(ops):
    cur_op = list(map(int, input().split()))
    if cur_op[0] == 1:
        cur_row = cur_op[1] - 1
        mt[cur_row] = [mt[cur_row][-1]] + mt[cur_row][:-1]
    elif cur_op[0] == 2:
        new_mt = copy.deepcopy(mt)
        for i in range(N):
            for j in range(N):
                new_mt[j][N-i-1] = mt[i][j]
        mt = copy.deepcopy(new_mt)
for i in range(N):
    for j in range(N):
        print(mt[i][j], end = " ")
    print()