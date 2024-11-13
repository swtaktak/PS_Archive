import sys
input = sys.stdin.readline
t_case = int(input())
for _ in range(t_case):
    N = int(input())
    ans_list = [(0, 0) for _ in range(N+1)]

    for i in range(0, N+1):
        if i == 0:
            ans_list[0] = (1, 0)
        elif i == 1:
            ans_list[1] = (0, 1)
        else:
            ans_list[i] = (ans_list[i-1][0]+ans_list[i-2][0], ans_list[i-1][1]+ans_list[i-2][1])
    print("%d %d" %(ans_list[N][0], ans_list[N][1]))