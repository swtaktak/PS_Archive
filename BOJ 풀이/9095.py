import sys
input = sys.stdin.readline

test_N = int(input())

for t in range(test_N):
    N = int(input())

    answer_list = [0] * (N+1)

    for i in range(1, N+1):
        if i == 1:
            answer_list[i] = 1
        elif i == 2:
            answer_list[i] = 2
        elif i == 3:
            answer_list[i] = 4
        else:
            answer_list[i] = (answer_list[i-1] + answer_list[i-2] + answer_list[i-3])
    print(answer_list[N])