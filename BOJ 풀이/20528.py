import sys
input = sys.stdin.readline

N = int(input())
word_list = list(map(str, input().rstrip().split()))


if N == 1:
    print(1)
else:
    letter = word_list[0][0]
    
    judge = True
    for i in range(1, N):
        cur_first = word_list[i][0]
        if letter != cur_first:
            judge = False
            break
    if judge:
        print(1)
    else:
        print(0)