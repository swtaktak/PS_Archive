import sys
input = sys.stdin.readline

N = int(input())
per_list = []
min_pow = 1e7

for _ in range(N):
    per_list.append(int(input()))
    
per_list.sort()

for i in range(0, N // 2):
    cur_pow = per_list[i] + per_list[N-i-1]
    min_pow = min(min_pow, cur_pow)

print(min_pow)
