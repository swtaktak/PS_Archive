import sys
input = sys.stdin.readline

N = int(input())
rope_list = []

for _ in range(N):
    cur_r = int(input())
    rope_list.append(cur_r)
    
rope_list.sort()

ans = -1

for r in rope_list:
    cur_w = N * r
    ans = max(ans, cur_w)
    N -= 1

print(ans)