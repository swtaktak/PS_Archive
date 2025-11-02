import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, N+1):
    cur_row =' ' * (N-i) + '*' * (2 * i - 1)
    print(cur_row)
for i in range(N-1, 0, -1):
    cur_row =' ' * (N-i) + '*' * (2 * i - 1)
    print(cur_row)