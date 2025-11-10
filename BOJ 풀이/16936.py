import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
num_list = list(map(int, input().split()))
num_dict = {}

# 해시로 값을 찾기 쉽게 만든다.
# 쓴거 또 안 쓰게 관리필요
for n in num_list:
    if n not in num_list:
        num_dict[n] += 1
    else:
        num_dict[n] = 1

# 기준선이다.    
start_num = max(num_list)
q.append(start_num)

# 왼쪽 반대방향
judge = True
while judge:
    cur_num = q.popleft()
    if cur_num % 2 == 0 and cur_num // 2 in num_dict and num_dict[cur_num // 2] > 0:
        next = cur_num // 2
        num_dict[next] -= 1
        q.appendleft(cur_num)
        q.appendleft(next)
        judge = True
    elif cur_num * 3 in num_dict and num_dict[cur_num * 3] > 0:
        next = cur_num * 3
        num_dict[next] -= 1
        q.appendleft(cur_num)
        q.appendleft(next)
        judge = True
    else:
        q.appendleft(cur_num)
        judge = False
    
# 오른쪽 정방향
judge = True
while judge:
    cur_num = q.pop()
    if cur_num % 3 == 0 and cur_num // 3 in num_dict and num_dict[cur_num // 3] > 0:
        next = cur_num // 3
        num_dict[next] -= 1
        q.append(cur_num)
        q.append(next)
        judge = True
    elif cur_num * 2 in num_dict and num_dict[cur_num * 2] > 0:
        next = cur_num * 2
        num_dict[next] -= 1
        q.append(cur_num)
        q.append(next)
        judge = True
    else:
        q.append(cur_num)
        judge = False

for cur_q in q:
    print(cur_q, end = " ")