import sys
input = sys.stdin.readline

start, Q = map(int, input().split())
salary_list = [start]
step = 1
while True:
    if start % step == 0:
        salary_list.append(start + step)
        start = start + step
    else:
        salary_list.append(start + (step - (start % step)))
        start = start + (step - (start % step))
    if start == step ** 2:
        same_cut = step
        break
    else:
        step += 1
        
for _ in range(Q):
    N = int(input())
    if N <= same_cut:
        print(salary_list[N])
    else:
        print(salary_list[-1] + same_cut * (N - same_cut))
        