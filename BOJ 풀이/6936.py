# cycle을 구하고, 최소공배수를 구하는 방식
import sys
input = sys.stdin.readline

def lcm(a, b):
    pa, pb = a, b
    while b > 0:
        a, b = b, a % b
    return pa * pb // a

def cycle(start):
    cur_v = start
    cur_cycle = 0
    while not visited[cur_v]:
        visited[cur_v] = True
        cur_v = seat_list[cur_v]
        cur_cycle += 1
    return cur_cycle

while True:
    monkey = int(input())
    if monkey == 0:
        break
    else:
        seat_list = [0] * (monkey + 1)
        for _ in range(monkey):
            start, end = map(int, input().split())
            seat_list[start] = end
            
        cycle_len_list = []
        visited = [False] * (monkey + 1)
        
        for i in range(1, monkey + 1):
            if not visited[i]:
                cur_cycle = cycle(i)
                cycle_len_list.append(cur_cycle)
        if len(cycle_len_list) == 1:
            print(cycle_len_list[0])
        else:
            ans = 1
            for i in range(0, len(cycle_len_list)):
                cur_len = cycle_len_list[i]
                if i == 0:
                    ans = cur_len
                else:
                    ans = lcm(ans, cur_len)
            print(ans)