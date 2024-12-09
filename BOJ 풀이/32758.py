import sys
input = sys.stdin.readline

def total_get(N, cur_ev):
    cnt = N
    while True:
        q, r = N // cur_ev, N % cur_ev
        if q + r < cur_ev:
            break
        else:
            cnt += q
            N = q + r
    cnt += q 
    return cnt

prod_type = int(input())
event_list = list(map(int, input().split()))
goal_list = list(map(int, input().split()))

for T in range(prod_type):
    cur_ev, cur_goal = event_list[T], goal_list[T]
    if cur_goal < cur_ev:
        print(cur_goal, end = " ")
    elif cur_ev == 1:
        print(1, end = " ")
    else:
        answer = cur_goal
        start = 1
        end = cur_goal
        while start <= end:
            mid = (start + end) // 2
            cur_get = total_get(mid, cur_ev)
            if cur_get < cur_goal:
                start = mid + 1
            else:
                end = mid - 1
                if answer > mid:
                    answer = mid
        print(answer, end = " ")