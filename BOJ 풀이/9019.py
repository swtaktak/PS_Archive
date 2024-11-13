import sys
from collections import deque
input = sys.stdin.readline
def ord_D(num):
    result = num * 2
    return (result) % 10000
def ord_S(num):
    return (num - 1)% 10000
def ord_L(num):
    first_digit = num // 1000
    result = (num % 1000) * 10 + first_digit 
    return result
def ord_R(num):
    last_digit = num % 10
    result = (num // 10) + last_digit * 1000
    return result



def bfs(cur_num, end_num, ord_str, visited):
    queue = deque()
    queue.append((cur_num, ord_str))
    visited[cur_num] = True
        
    while queue:
        num, ord = queue.popleft()
        if num == end_num:
            print(ord)
            break
        else:
            if not visited[ord_D(num)]:
                visited[ord_D(num)] = True
                queue.append((ord_D(num), ord + 'D'))
                
            if not visited[ord_S(num)]:
                visited[ord_S(num)] = True
                queue.append((ord_S(num), ord + 'S'))
                
            if not visited[ord_L(num)]:
                visited[ord_L(num)] = True
                queue.append((ord_L(num), ord + 'L'))
                
            if not visited[ord_R(num)]:
                visited[ord_R(num)] = True
                queue.append((ord_R(num), ord + 'R'))
    return 'impossible'

t_case = int(input())
for _ in range(t_case):
    start_num, end_num = map(int, input().split())
    answer = ''
    visited = [False] * 10000
    answer = bfs(start_num, end_num, '', visited)