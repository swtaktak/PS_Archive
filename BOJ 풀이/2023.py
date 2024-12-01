# 8천만까지 모두 소수를 뽑는 것은 무리!
# bfs로 해결하자.
from collections import deque
def is_prime(N):
    if N <= 1:
        return False
    else:
        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                return False
    return True
 
 
N = int(input())
answer_list = []

add_list = ['1', '3', '7', '9']
q = deque()
q.append(2)
q.append(3)
q.append(5)
q.append(7)
while q:
    cur_num = q.popleft()
    if len(str(cur_num)) == N:
        print(cur_num)
    else:
        for a in add_list:
            next_num = int(str(cur_num) + a)
            if is_prime(next_num):
                q.append(next_num)