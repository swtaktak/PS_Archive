import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs(n):
    q = deque()
    q.append(1)
    
    while q:
        cur_num = q.popleft()
        if cur_num % n == 0 and len(str(cur_num)) <= 100:
            res_list[0] = cur_num
            break
        else:
            zero_add = cur_num * 10
            if res_list[zero_add % n] == 2:
                if len(str(zero_add)) <= 100:
                    res_list[zero_add % n] = zero_add
                    q.append(zero_add)
            one_add = cur_num * 10 + 1
            if res_list[one_add % n] == 2:
                if len(str(one_add)) <= 100:
                    res_list[one_add % n] = one_add
                    q.append(one_add)                  
    

for _ in range(T):
    n = int(input())
    res_list = [2 for _ in range(n)]
    bfs(n)
    if res_list[0] == 2:
        print('BRAK')
    else:
        print(res_list[0])