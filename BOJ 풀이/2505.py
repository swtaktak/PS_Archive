import sys
input = sys.stdin.readline

N = int(input())
# 1-base 맞추기 위함.
num_list = [0] + list(map(int, input().split()))

# 좌좌
ll_list_success_flag = True
ll_list = num_list.copy()
ans_list = []
for _ in range(2):
    for i in range(1, N + 1):
        if ll_list[i] != i:
            i_idx = ll_list.index(i)
            ll_list = ll_list[0:i] + ll_list[i_idx:i-1:-1] + ll_list[i_idx+1:]
            ans_list.append((i, i_idx))
            break
# 좌좌 성공여부 점검
for i in range(1, N+1):
    if ll_list[i] != i:
        ll_list_success_flag = False

if ll_list_success_flag and len(ans_list) == 2:
    for i in range(2):
        print("%d %d" %(ans_list[i][0], ans_list[i][1]))
elif ll_list_success_flag and len(ans_list) == 1:
    print("%d %d" %(ans_list[0][0], ans_list[0][1]))
    print("1 1")
elif ll_list_success_flag and len(ans_list) == 0:
    print("1 1")
    print("1 1")
else:
    #우좌 해야 한다.
    rl_list = num_list.copy()
    ans_list = []
    for i in range(N, 0, -1):
        if rl_list[i] != i:
            i_idx = rl_list.index(i)
            rl_list = rl_list[0:i_idx] + rl_list[i:i_idx-1:-1] + rl_list[i+1:]
            ans_list.append((i_idx, i))
            break
    for i in range(1, N + 1):
        if rl_list[i] != i:
            i_idx = rl_list.index(i)
            rl_list = rl_list[0:i] + rl_list[i_idx:i-1:-1] + rl_list[i_idx+1:]
            ans_list.append((i, i_idx))
            break
    if len(ans_list) == 2:
        for i in range(2):
            print("%d %d" %(ans_list[i][0], ans_list[i][1]))
    else:
        print("%d %d" % (ans_list[0][0], ans_list[0][1]))
        print("1 1")