import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
answer = [-1] * N
stack = []
for i in range(0, N):
    if not stack:
        stack.append([num_list[i], i])
    else:
        while stack:
            if stack[-1][0] < num_list[i]:
                answer[stack[-1][1]] = num_list[i]
                stack.pop()
            else:
                break
        stack.append([num_list[i], i])
for i in range(N):
    if i < N-1:
        print(answer[i], end = " ")
    else:
        print(answer[i])
        
# 효율답안은, 인덱스만 담으면 됨.

