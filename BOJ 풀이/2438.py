import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, N+1):
    cur_row = '*' * i
    print(cur_row)
    