import sys
import heapq
input = sys.stdin.readline

cnt =0
card_list = []
heapq.heapify(card_list)

N = int(input())
for _ in range(N):
    cur_cards = int(input())
    heapq.heappush(card_list, cur_cards)
    
while len(card_list) >= 2:
    c1 = heapq.heappop(card_list)
    c2 = heapq.heappop(card_list)
    cnt += (c1 + c2)
    heapq.heappush(card_list, c1 + c2)
print(cnt)