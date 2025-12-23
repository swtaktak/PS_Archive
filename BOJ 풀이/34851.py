import sys
input = sys.stdin.readline

N = int(input())
P = 10**9 + 7

num_list = list(map(int, input().split()))
ans = 0
for i in range(1, N + 1):
    if i == 1:
        if 1 in [num_list[0], num_list[1]]:
            ans = (num_list[0] + num_list[1]) % P
        else:
            ans = (num_list[0] * num_list[1]) % P
    else:
        if num_list[i] == 1:
            ans += 1
        else:
            ans = (ans * num_list[i]) % P
        
print(ans % P)