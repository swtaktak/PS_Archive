import sys
input = sys.stdin.readline
N = int(input())
num_list = [True for _ in range(1000001)]
num_list[0] = False
num_list[1] = False
for i in range(2, int(1000001 ** 0.5) + 1):
    if num_list[i]:
        for j in range(2*i, 1000001, i):
            num_list[j] = False

if N < 8 :
    print(-1)
elif N % 2 == 0:
    # 4 + ?
    for cur_num in range(2, (N-4)//2 + 1):
        if num_list[cur_num] and num_list[(N-4) - cur_num]:
            break
    print("%d %d %d %d" %(2, 2, cur_num, N-cur_num-4))
else:
    # 5 + ?
    for cur_num in range(2, (N-5)//2 + 1):
        if num_list[cur_num] and num_list[(N-5) - cur_num]:
            break
    print("%d %d %d %d" %(2, 3, cur_num, N-cur_num-5))