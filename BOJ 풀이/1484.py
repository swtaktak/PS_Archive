import sys
input = sys.stdin.readline

N = int(input())
answer_list = []

for i in range(1, int(N ** 0.5) + 1):
    left = i
    right = N // i
    if N % i == 0 and i < N // i:
        if (left + right) % 2 == 0:
            answer_list.append((left + right) // 2)

if len(answer_list) == 0:
    print(-1)
else:
    for i in range(len(answer_list)-1,-1,-1):
        print(answer_list[i], end = "\n")