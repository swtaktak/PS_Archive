import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    files = int(input())
    file_list = list(map(int, input().split()))
    heapq.heapify(file_list)
    answer = 0
    while len(file_list) > 1:
        first = heapq.heappop(file_list)
        second = heapq.heappop(file_list)
        answer += (first + second)
        heapq.heappush(file_list, first+second)
    print(answer)