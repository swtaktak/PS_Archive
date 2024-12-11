import sys
input = sys.stdin.readline

def is_hap(cur_pick):
    card1 = cur_pick[0]
    card2 = cur_pick[1]
    card3 = cur_pick[2]
    hap_flag = True
    # 속성 판정
    for i in range(0, 3):
        if card1[i] == card2[i]:
            if card1[i] != card3[i]:
                hap_flag = False
        else:
            if card1[i] == card3[i] or card2[i] == card3[i]:
                hap_flag = False
    return hap_flag

def hap_dfs(level, cur_pos):
    global hap_list
    if level == 3:
        cur_pick_cards = []
        for p in picked_card:
            cur_pick_cards.append(card_list[p])
        if is_hap(cur_pick_cards):
            cur_hap = picked_card.copy()
            for i in range(3):
                cur_hap[i] += 1
            hap_list.append(cur_hap)
        return
    for i in range(cur_pos, 9):
        if not visited[i]:
            visited[i] = True
            picked_card.append(i)
            hap_dfs(level + 1, i)
            visited[i] = False
            picked_card.pop()

card_list = []
hap_list = []
for _ in range(9):
    cur_card = list(map(str, input().rstrip().split()))
    card_list.append(cur_card)
visited = [False] * 9
picked_card = []
hap_dfs(0, 0)

records = int(input())
left_hap = len(hap_list)
score = 0
final_flag = False
for _ in range(records):
    cur_r = list(map(str, input().rstrip().split()))
    if cur_r[0] == 'H':
        call_list = [int(x) for x in cur_r[1:]]
        call_list.sort()
        if call_list in hap_list:
            score += 1
            hap_list.remove(call_list)
            left_hap -= 1
        else:
            score -= 1
    else:
        if not final_flag and left_hap == 0:
            score += 3
            final_flag = True
        else:
            score -= 1
print(score)