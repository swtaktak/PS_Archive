import sys
input = sys.stdin.readline
N = int(input())
dduk_list = list(map(int, input().split()))
dduk_cnt = [0] * 50001

for d in dduk_list:
    dduk_cnt[d] += 1
    
print(max(dduk_cnt))