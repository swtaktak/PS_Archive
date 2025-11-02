import sys
from collections import deque
input = sys.stdin.readline

card_dict = {}
N = int(input())
card_queue = deque()

for i in range(1, N+1):
    card_queue.append(i)

action_list = list(map(int, input().split()))
result_card = N

for a in action_list:
    if a == 1:
        cur_card = card_queue.popleft()    
    elif a == 2:
        prev_card = card_queue.popleft()
        cur_card = card_queue.popleft()
        card_queue.appendleft(prev_card)
    else:
        cur_card = card_queue.pop()
    
    # 카드 처리부
    card_dict[cur_card] = result_card
    result_card -= 1

for i in range(1, N+1):
    print(card_dict[i], end = " ")