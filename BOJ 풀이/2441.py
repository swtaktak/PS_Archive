import sys
input = sys.stdin.readline

N = int(input())
for i in range(N, 0, -1):
    cur_row =' ' * (N-i) + '*' * i
    print(cur_row)
    