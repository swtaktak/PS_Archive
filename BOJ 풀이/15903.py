import sys
import heapq
input = sys.stdin.readline

N, change = map(int, input().split())
num_list = list(map(int, input().split()))
ans = sum(num_list)
heapq.heapify(num_list)


for _ in range(change):
    num1 = heapq.heappop(num_list)
    num2 = heapq.heappop(num_list)
    ans += (num1 + num2)
    heapq.heappush(num_list, num1 + num2)
    heapq.heappush(num_list, num1 + num2)

print(ans)