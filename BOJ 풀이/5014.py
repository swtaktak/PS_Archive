import sys
from collections import deque
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
floors, start, goal, up, down = map(int, input().split())
# case 1 만일 up이 없는데, goal이 더 높으면 계단
if up == 0:
    if start < goal:
        print('use the stairs')
    elif down == 0:
        if start != goal:
            print('use the stairs')
        else:
            print(0)
    else:
        if (start - goal) % down == 0:
            print((start-goal)//down)
        else:
            print('use the stairs')
# case 2 만일 down이 없는데, goal이 더 낮아도 계단
elif down == 0:
    if start > goal:
        print('use the stairs')
    elif up == 0:
        if start != goal:
            print('use the stairs')
        else:
            print(0)
    else:
        if (goal - start) % up == 0:
            print((goal-start)//up)
        else:
            print('use the stairs')
else:
    d = gcd(up, down)
    if (goal-start) % d != 0:
        print('use the stairs')
    else:
        visited = [False] * (floors+1)
        visited[start] = True
        q = deque()
        q.append((start, 0))
        success_flag = False
        while q:
            cur_f, cur_turn = q.popleft()
            if cur_f == goal:
                print(cur_turn)
                success_flag = True
                break
            else:
                if cur_f + up <= floors and not visited[cur_f + up]:
                    visited[cur_f + up] = True 
                    q.append((cur_f + up, cur_turn + 1))
                if cur_f - down >= 1 and not visited[cur_f - down]:
                    visited[cur_f - down] = True
                    q.append((cur_f - down, cur_turn + 1))           
        if not success_flag:
            print('use the stairs')