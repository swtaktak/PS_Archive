import sys
from collections import deque
input = sys.stdin.readline
# 절반을 섞어 앞을 먼저 하는 것은 in_suffle
# 절반을 섞어 뒤를 먼저 하는 것은 out_suffle
# ABC  DE     AB  CDE  CADBE

def outcard(card):
    card_list = [i for i in range(1, card + 1)]
    count = 0
    while True:
        count += 1
        left = deque()
        right = deque()
        # step 1: card를 left_right 으로 나눈다.
        if card % 2 == 0:
            for i in range(card):
                if i < card // 2: 
                    left.append(card_list[i])
                else:
                    right.append(card_list[i])
        else:
             for i in range(card):
                if i <= card // 2:
                    left.append(card_list[i])
                else:
                    right.append(card_list[i])
        card_list = []
        for i in range(card):
            if i % 2 == 0:
                cur_elt = left.popleft()
                card_list.append(cur_elt)
            else:
                cur_elt = right.popleft()
                card_list.append(cur_elt)
        if card_list[0] == 1 and card_list[1] == 2:
            break
    return count


def incard(card):
    card_list = [i for i in range(1, card + 1)]
    count = 0
    while True:
        count += 1
        left = deque()
        right = deque()
        # step 1: card를 left_right 으로 나눈다.
        if card % 2 == 0:
            for i in range(card):
                if i < card// 2:
                    left.append(card_list[i])
                else:
                    right.append(card_list[i])
        else:
             for i in range(card):
                if i < card // 2:
                    left.append(card_list[i])
                else:
                    right.append(card_list[i])
        card_list = []
        for i in range(card):
            if i % 2 == 0:
                cur_elt = right.popleft()
                card_list.append(cur_elt)
            else:
                cur_elt = left.popleft()
                card_list.append(cur_elt)
        if card_list[0] == 1 and card_list[1] == 2:
            break
    return count

card, order = map(str, input().rstrip().split())
card = int(card)

if card == 1:
    print(1)

else:
    if order == 'in':
        print(incard(card))
    else:
        print(outcard(card))

