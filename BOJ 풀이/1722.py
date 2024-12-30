# N이 20이라 DFS 불가.
import sys
import math
input = sys.stdin.readline

def xth_to_seq(x, N):
    visited = [False] * (N+1)
    answer_seq = []
    x = x-1
    while len(answer_seq) < N:
        cur_fact = math.factorial(N-1-len(answer_seq))
        cur_goal = (x // cur_fact) + 1
        cur_step = 0
        for i in range(1, N+1):
            if not visited[i]:
                cur_step += 1
                if cur_step == cur_goal:
                    visited[i] = True
                    answer_seq.append(i)
        x = x % cur_fact
    return answer_seq
        
def seq_to_xth(seq, N):
    visited = [False] * (N+1)
    x = 0
    for i in range(N):
        cur_fact = math.factorial(N-1-i)
        cur_step = 0
        cur_num = seq[i]
        for j in range(1, N+1):
            if not visited[j]:
                cur_step += 1
                if j == cur_num:
                    visited[j] = True
                    x += cur_fact * (cur_step - 1)
                    break
    return x + 1

N = int(input())
q_list = list(map(int, input().split()))

if q_list[0] == 1:
    answer_seq = xth_to_seq(q_list[1], N)
    for a in answer_seq:
        print(a, end = " ")20
1 2432902008176640000
elif q_list[0] == 2:
    goal_seq = q_list[1:]
    answer_x = seq_to_xth(goal_seq, N)
    print(answer_x)