import sys
import heapq

input = sys.stdin.readline

T = int(input())
for cur_case in range(1, T+1):
    total_q, time_l = map(int, input().split())
    cur_time = 0
    spend_list = list(map(int, input().split()))
    solved_list = []
    
    while spend_list:
        cur_solve = heapq.heappop(spend_list)
        if cur_time + cur_solve > time_l:
            break
        else:
            solved_list.append(cur_solve)
            cur_time += cur_solve
    
    total_time = 0
    solved = len(solved_list)
    solved_list.sort()
    for i in range(solved):
        total_time += ((solved - i) * solved_list[i])
    
    print("Case %d: %d %d %d" %(cur_case, solved, cur_time, total_time))  