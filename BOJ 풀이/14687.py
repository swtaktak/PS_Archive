import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
if N % 2 == 0:
    cutline = N // 2
else:
    cutline = N // 2 + 1
small_wave = num_list[:cutline]
big_wave = num_list[cutline:]
big_wave.sort(reverse = True)

answer = []
for i in range(N):
    if i % 2 == 0:
        answer.append(small_wave.pop())
    else:
        answer.append(big_wave.pop())

for i in range(N):
    if i < N-1:
        print(answer[i], end = " ")
    else:
        print(answer[i])
