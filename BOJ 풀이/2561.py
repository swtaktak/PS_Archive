import sys
input = sys.stdin.readline

def left_change(ll_list, ans_list):
    for i in range(1, N + 1):
        if ll_list[i] != i:
            i_idx = ll_list.index(i)
            ll_list = ll_list[0:i] + ll_list[i_idx:i-1:-1] + ll_list[i_idx+1:]
            ans_list.append((i, i_idx))
            break
    return ll_list, ans_list

def right_change(rl_list, ans_list):
    for i in range(N, 0, -1):
        if rl_list[i] != i:
            i_idx = rl_list.index(i)
            rl_list = rl_list[0:i_idx] + rl_list[i:i_idx-1:-1] + rl_list[i+1:]
            ans_list.append((i_idx, i))
            break
    return rl_list, ans_list

def success(num_list):
    for i in range(1, N+1):
        if i != num_list[i]:
            return False
    return True

N = int(input())
# 1-base 맞추기 위함.
num_list = [0] + list(map(int, input().split()))

ans_list = []


# 1회차부터 시작.
l_list, l_ans_list = left_change(num_list.copy(), ans_list.copy())
r_list, r_ans_list = right_change(num_list.copy(), ans_list.copy())

if len(l_ans_list) == 0 and len(r_ans_list) == 0:
    print('1 1')
    print('1 1')
    print('1 1')

elif success(l_list):
    # 1회차에서 클리어
    print("%d %d" %(l_ans_list[0][0], l_ans_list[0][1]))
    print("1 1")
    print("1 1")
    
else:
    # 2회차 돌입
    # 좌좌, 좌우, 우좌, 우우 네가지를 다 봐야 한다.
    # 넷 다 실패시, 넷 중 마지막으로 left change를 해서 성공하는지 봐야 한다.
    ll_list, ll_ans_list = left_change(l_list.copy(), l_ans_list.copy())
    lr_list, lr_ans_list = right_change(l_list.copy(), l_ans_list.copy())
    rl_list, rl_ans_list = left_change(r_list.copy(), r_ans_list.copy())
    rr_list, rr_ans_list = right_change(r_list.copy(), r_ans_list.copy())
    if success(ll_list):
        print("%d %d" %(ll_ans_list[0][0], ll_ans_list[0][1]))
        print("%d %d" %(ll_ans_list[1][0], ll_ans_list[1][1]))
        print("1 1")
    elif success(lr_list):
        print("%d %d" %(lr_ans_list[0][0], lr_ans_list[0][1]))
        print("%d %d" %(lr_ans_list[1][0], lr_ans_list[1][1]))
        print("1 1")
    elif success(rl_list):
        print("%d %d" %(rl_ans_list[0][0], rl_ans_list[0][1]))
        print("%d %d" %(rl_ans_list[1][0], rl_ans_list[1][1]))
        print("1 1")
    elif success(rr_list):
        print("%d %d" %(rr_ans_list[0][0], rr_ans_list[0][1]))
        print("%d %d" %(rr_ans_list[1][0], rr_ans_list[1][1]))
        print("1 1")
    else:
        # 넷 중 하나는 반드시 클리어
        lll_list, lll_ans_list = left_change(ll_list.copy(), ll_ans_list.copy())
        lrl_list, lrl_ans_list = left_change(lr_list.copy(), lr_ans_list.copy())
        rll_list, rll_ans_list = left_change(rl_list.copy(), rl_ans_list.copy())
        rrl_list, rrl_ans_list = left_change(rr_list.copy(), rr_ans_list.copy())
        print(lll_ans_list, lrl_ans_list, rll_ans_list, rrl_ans_list)
        if success(lll_list):
            print("%d %d" %(lll_ans_list[0][0], lll_ans_list[0][1]))
            print("%d %d" %(lll_ans_list[1][0], lll_ans_list[1][1]))
            print("%d %d" %(lll_ans_list[2][0], lll_ans_list[2][1]))
        elif success(lrl_list):
            print("%d %d" %(lrl_ans_list[0][0], lrl_ans_list[0][1]))
            print("%d %d" %(lrl_ans_list[1][0], lrl_ans_list[1][1]))
            print("%d %d" %(lrl_ans_list[2][0], lrl_ans_list[2][1]))
        elif success(rll_list):
            print("%d %d" %(rll_ans_list[0][0], rll_ans_list[0][1]))
            print("%d %d" %(rll_ans_list[1][0], rll_ans_list[1][1]))
            print("%d %d" %(rll_ans_list[2][0], rll_ans_list[2][1]))
        else:
            print("%d %d" %(rrl_ans_list[0][0], rrl_ans_list[0][1]))
            print("%d %d" %(rrl_ans_list[1][0], rrl_ans_list[1][1]))
            print("%d %d" %(rrl_ans_list[2][0], rrl_ans_list[2][1]))