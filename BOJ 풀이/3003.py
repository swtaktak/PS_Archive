import sys
input = sys.stdin.readline
have_list = list(map(int, input().split()))
need_list = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(need_list[i] - have_list[i], end = " ")
