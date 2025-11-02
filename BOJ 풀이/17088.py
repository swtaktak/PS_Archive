# 경우는 9개
import sys
input = sys.stdin.readline
change = [-1, 0, 1]
N = int(input())
num_list = list(map(int, input().split()))

if N <= 2:
    print(0)
else:
    answer = N + 1
    for m_1 in change:
        for m_2 in change:
            cur_list = []
            cur_list.append(num_list[0] + m_1)
            cur_list.append(num_list[1] + m_2)
            d = cur_list[1] - cur_list[0]
            
            while len(cur_list) < N:
                cur_list.append(cur_list[-1] + d)
            
            judge = True
            cur_ans = 0
            for i in range(N):
                if abs(cur_list[i] - num_list[i]) >= 2:
                    judge = False
                    break
                elif abs(cur_list[i] - num_list[i]) == 1:
                    cur_ans += 1
            if judge:
                answer = min(answer, cur_ans)
    if answer == N + 1:
        print(-1)
    else:
        print(answer)