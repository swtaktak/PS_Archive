# 5000
# Odd Permutation, Even Permutation
import sys
input = sys.stdin.readline

N = int(input())
before_list = list(map(int, input().split()))
after_list = list(map(int, input().split()))

visited = [False for _ in range(N + 1)]
b_to_a = dict()

for i in range(N):
    b_to_a[before_list[i]] = after_list[i]
    
total_change = 0
for i in range(1, N + 1):
    if not visited[i]:
        cur_change = 0
        cur_bread = i
        while not visited[cur_bread]:
            visited[cur_bread] = True
            next_bread = b_to_a[cur_bread]
            cur_bread = next_bread
            cur_change += 1
        total_change += (cur_change - 1)

if total_change % 2 == 0:
    print("Possible")
else:
    print("Impossible")