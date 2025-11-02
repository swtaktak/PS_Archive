import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * (N+1)
add_list = []
stack = []

for _ in range(M):
    cur_num = int(input())
    stack.append(cur_num)
    visited[cur_num] = True
    
for i in range(1, N+1):
    if not visited[i]:
        add_list.append(i)

add_list.sort(reverse = True)
stack = stack[::-1]
ans_list = []


while stack:
    if add_list and stack[-1] < add_list[-1]:
        ans_list.append(stack.pop())
    elif add_list and stack[-1] > add_list[-1]:
        ans_list.append(add_list.pop())
    else:
        ans_list.append(stack.pop())

while add_list:
    ans_list.append(add_list.pop())
    
for a in ans_list:
    print(a)
            
