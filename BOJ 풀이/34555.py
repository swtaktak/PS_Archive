import sys
input = sys.stdin.readline

N = int(input())
answer_list = []

if N % 2 == 0:
    start = N // 2
else:
    start = (N + 1) // 2

answer_list.append(start)
sign = True
for i in range(1, N):
    prev = answer_list[-1]
    if sign:
        sign = False
        next = prev + i
    else:
        sign = True
        next = prev - i
    answer_list.append(next)
    
for a in answer_list:
    print(a, end = " ")