import sys
input = sys.stdin.readline

c = int(input())
for T in range(c):
    cur_list = list(map(int, input().split()))
    cur_std = cur_list[0]
    cur_score = sorted(cur_list[1:])
    min_s = cur_score[0]
    max_s = cur_score[-1]
    max_diff = 0
    for i in range(1, cur_std):
        max_diff = max(max_diff, cur_score[i] - cur_score[i-1])
    print("Class %d" %(T+1))
    print("Max %d, Min %d, Largest gap %d" % (max_s, min_s, max_diff))