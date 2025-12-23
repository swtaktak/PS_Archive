import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))
    
num_list.sort()
pos_score = -1
for i in range(1, N):
    pos_score = max(pos_score, num_list[i] + (N - i))

ans = 0
for i in range(0, N):
    if num_list[i] + N >= pos_score:
        ans += 1

print(ans)