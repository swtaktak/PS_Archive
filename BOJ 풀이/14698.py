import sys
import heapq
input = sys.stdin.readline
p = 1000000007
T = int(input())
for _ in range(T):
    N = int(input())
    ans = 1
    slime_list = list(map(int, input().split()))
    heapq.heapify(slime_list)
    
    while len(slime_list) > 1:
        first = heapq.heappop(slime_list)
        second = heapq.heappop(slime_list)
        ans *= (first * second) % p
        heapq.heappush(slime_list, first * second)
    print(ans % p)    