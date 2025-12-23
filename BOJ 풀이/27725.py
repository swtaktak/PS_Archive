import sys
input = sys.stdin.readline

N = int(input())
prime_list = list(map(int, input().split()))
K = int(input())

ans = 0

for p in prime_list:
    cur = p
    while K >= cur:
        ans += K // cur
        cur *= p
        
print(ans)