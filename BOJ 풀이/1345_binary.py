import sys
input = sys.stdin.readline

def check(a0, d, N):
    new_list = [a0 + i * d for i in range(0, N + 1)]
    same_flag = 2 # 2가 성공
    for i in range(N+1):
        if num_list[i] > int(new_list[i]):
            same_flag = 1
            break
        elif num_list[i] < int(new_list[i]):
            same_flag = 0
            break
    return same_flag

N, a0 = map(int, input().split())
num_list = [a0] + list(map(int, input().split()))

if N == 0:
    print(0)
else:
    answer = 10 ** 7
    decrease_flag = False
    for i in range(1, N+1):
        if num_list[i] < num_list[i-1]:
            decrease_flag = True
            break

    if decrease_flag:
        print(-1)
    else:
        start = 0
        end = 10 ** 6
        success_flag = False
        while end - start > 1e-10:
            mid = (start + end) / 2
            flag = check(a0, mid, N)
            if flag == 2:
                success_flag = True
                answer = min(mid, answer)
                end = mid
            elif flag == 1:
                start = mid
            else:
                end = mid
        if answer != 10 ** 7:
            print(answer)
        else:
            print(-1)